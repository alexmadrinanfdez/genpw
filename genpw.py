import string
import secrets

def generate_password(length):
    if length <= 0:
        raise ValueError("Length must be positive")
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))
