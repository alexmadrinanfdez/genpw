import argparse
import secrets
import string

def generate_password(length, include, strict):
    if length <= 0:
        raise ValueError("Length must be positive")

    lower = "lower" in include
    upper = "upper" in include
    digits = "digits" in include
    punctuation = "punctuation" in include

    pool = create_character_pool(lower, upper, digits, punctuation)
    password = ''.join(secrets.choice(pool) for _ in range(length))
    
    if strict:
        if length < len(include):
            raise ValueError("Length is insufficient for strict rules")
        # If generated password does not meet criteria, generate a new one
        if not (
            (not lower or any(c.islower() for c in password))
            and (not upper or any(c.isupper() for c in password))
            and (not digits or any(c.isdigit() for c in password))
            and (not punctuation or any(c in string.punctuation for c in password))
        ):
            return generate_password(length, include, strict)
    
    return password

def create_character_pool(lower, upper, digits, punctuation):
    pool = ""
    if lower:
        pool += string.ascii_lowercase
    if upper:
        pool += string.ascii_uppercase
    if digits:
        pool += string.digits
    if punctuation:
        pool += string.punctuation
    if not pool:
        raise ValueError("At least one character type must be selected")
    return pool

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("length", type=int,
                        help="Number of characters in the generated password")
    parser.add_argument("--include", nargs="+", 
                        choices=["lower", "upper", "digits", "punctuation"],
                        default=["lower", "upper", "digits"],
                        help="Character types to include in the password")
    parser.add_argument("--strict", action="store_true",
                        help="Enforce at least one character from each selected type")

    args = parser.parse_args()
    try:
        password = generate_password(args.length, args.include, args.strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        parser.error(str(e))