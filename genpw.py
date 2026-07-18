import argparse
import secrets
import string


CHARS_PER_TYPE = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digits": string.digits,
    "punctuation": string.punctuation
}


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
    for char_type in include:
        pool += CHARS_PER_TYPE[char_type]
        if strict:
            required.append(secrets.choice(CHARS_PER_TYPE[char_type]))
    # Fill the rest of the password
    remaining = [secrets.choice(pool) for _ in range(length - len(required))]
    pw_chars = required + remaining
    # Shuffle the password characters
    secrets.SystemRandom().shuffle(pw_chars)

    return ''.join(pw_chars)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate a secure password",
        suggest_on_error=True)
    
    parser.add_argument(
        "length",
        nargs='?', default=10, type=int,
        help="Number of characters in the generated password")
    parser.add_argument(
        "-e", "--exclude",
        nargs="+", choices=CHARS_PER_TYPE.keys(),
        help="Character types to exclude from the password")
    parser.add_argument(
        "-s", "--strict",
        action="store_true",
        help="Enforce at least one character from each selected type")

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.include = set(CHARS_PER_TYPE.keys())
    if args.exclude:
        args.include -= set(args.exclude)
    
    try:
        validate_inputs(args)
        password = generate_password(args.length, args.include, args.strict)
        print(f"Generated Password: {password}")
    except ValueError as e:
        parser.error(str(e))