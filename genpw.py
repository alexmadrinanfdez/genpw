import argparse
import secrets
import string

def generate_password(length, lower, upper, digits, punctuation, strict):
    if length <= 0:
        raise ValueError("Length must be positive")
    
    alphabet = ""
    if lower:
        alphabet += string.ascii_lowercase
    if upper:
        alphabet += string.ascii_uppercase
    if digits:
        alphabet += string.digits
    if punctuation:
        alphabet += string.punctuation
    if not alphabet:
        raise ValueError("At least one character type must be selected")

    password = ''.join(secrets.choice(alphabet) for i in range(length))
    
    if strict:
        if length < sum((lower, upper, digits, punctuation)):
            raise ValueError("Length is insufficient for strict rules")
        # If generated password does not meet criteria, generate a new one
        if not (
            (not lower or any(c.islower() for c in password))
            and (not upper or any(c.isupper() for c in password))
            and (not digits or any(c.isdigit() for c in password))
            and (not punctuation or any(c in string.punctuation for c in password))
        ):
            return generate_password(length, lower, upper, digits, punctuation, strict)
    
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("length", type=int,
                        help="Number of characters in the generated password")
    parser.add_argument("--lower", action="store_true",
                        help="Include lowercase letters")
    parser.add_argument("--upper", action="store_true",
                        help="Include uppercase letters")
    parser.add_argument("--digits", action="store_true",
                        help="Include digits")
    parser.add_argument("--punctuation", action="store_true",
                        help="Include punctuation")
    parser.add_argument("--strict", action="store_true",
                        help="Enforce at least one character from each selected type")

    args = parser.parse_args()
    try:
        password = generate_password(args.length, args.lower, args.upper, args.digits, args.punctuation, args.strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        parser.error(str(e))