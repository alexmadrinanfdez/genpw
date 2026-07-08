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
    # Create character pool and start password with required characters
    pool, required = '', []
    if "lower" in include:
        pool += string.ascii_lowercase
        if strict:
            required.append(secrets.choice(string.ascii_lowercase))
    if "upper" in include:
        pool += string.ascii_uppercase
        if strict:
            required.append(secrets.choice(string.ascii_uppercase))
    if "digits" in include:
        pool += string.digits
        if strict:
            required.append(secrets.choice(string.digits))
    if "punctuation" in include:
        pool += string.punctuation
        if strict:
            required.append(secrets.choice(string.punctuation))
    # Fill the rest of the password
    remaining_length = length - len(required)
    pw_chars = required + [secrets.choice(pool) for _ in range(remaining_length)]
    # Shuffle the password characters
    secrets.SystemRandom().shuffle(pw_chars)

    return ''.join(pw_chars)


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