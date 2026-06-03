import argparse
import secrets
import string

def validate_inputs(inputs):
    if inputs.length < 0:
        raise ValueError("Length must be a non-negative integer")
    if inputs.strict and inputs.length < len(inputs.include):
        raise ValueError("Length is insufficient for strict rules")
    if not inputs.include:
        raise ValueError("At least one character type must be included")

def generate_password(length, include, strict):
    pool = create_character_pool(include)
    password = ''.join(secrets.choice(pool) for _ in range(length))
    # If generated password does not meet criteria, generate a new one
    if strict and not password_rules_met(password, include):
        return generate_password(length, include, strict)
    
    return password

def create_character_pool(include):
    pool = ""
    if "lower" in include:
        pool += string.ascii_lowercase
    if "upper" in include:
        pool += string.ascii_uppercase
    if "digits" in include:
        pool += string.digits
    if "punctuation" in include:
        pool += string.punctuation
    return pool

def password_rules_met(password, include):
    if "lower" in include and not any(c.islower() for c in password):
        return False
    if "upper" in include and not any(c.isupper() for c in password):
        return False
    if "digits" in include and not any(c.isdigit() for c in password):
        return False
    if "punctuation" in include and not any(c in string.punctuation for c in password):
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("length", type=int,
                        help="Number of characters in the generated password")
    parser.add_argument("--exclude", nargs="+", 
                        choices=["lower", "upper", "digits", "punctuation"],
                        help="Character types to exclude from the password")
    parser.add_argument("--strict", action="store_true",
                        help="Enforce at least one character from each selected type")

    args = parser.parse_args()
    args.include = {"lower", "upper", "digits", "punctuation"}
    if args.exclude:
        args.include -= set(args.exclude)
    
    try:
        validate_inputs(args)
        password = generate_password(args.length, args.include, args.strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        parser.error(str(e))