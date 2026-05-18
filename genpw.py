import argparse
import secrets
import string

def generate_password(length, strict=False):
    if length <= 0:
        raise ValueError("Length must be positive")
    
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    
    if strict:
        if length < 3:
            raise ValueError("Length is insufficient for strict rules")
        # If generated password does not meet criteria, generate a new one
        if not (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            return generate_password(length, strict)
    
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a secure password")
    parser.add_argument("length", type=int,
                        help="Number of characters in the generated password")
    parser.add_argument("--strict", action="store_true",
                        help="Password must include uppercase, lowercase, and digits")

    args = parser.parse_args()
    try:
        password = generate_password(args.length, args.strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        parser.error(str(e))