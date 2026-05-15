import string
import secrets

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
    length = int(input("Enter the desired password length: "))
    strict_input = input("Should the password be strict (include uppercase, lowercase, and digits)? (y/n): ")
    strict = strict_input.lower() == 'y'
    
    try:
        password = generate_password(length, strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)