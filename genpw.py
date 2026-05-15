import string
import secrets

def generate_password(length, strict=False):
    if length <= 0:
        raise ValueError("Length must be positive")
    
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    
    if strict:
        # If generated password does not meet criteria, generate a new one
        if not (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            return generate_password(length, strict)
    
    return password
