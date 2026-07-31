# genpw

A command-line tool to generate secure, random passwords based on user requirements.

## Usage

Run the script from the root folder of the repository:

```bash
python3 -m genpw.genpw [options]
```

### Options

Use with the `--help` option to view the documentation on the different options.

```
% python3 -m genpw -h
usage: python3 -m genpw [-h]
                        [--exclude {lower,upper,digits,punctuation} [{lower,upper,digits,punctuation} ...]]
                        [--strict]
                        length

Generate a secure password

positional arguments:
  length                Number of characters in the generated password

options:
  -h, --help            show this help message and exit
  --exclude {lower,upper,digits,punctuation} [{lower,upper,digits,punctuation} ...]
                        Character types to exclude from the password
  --strict              Enforce at least one character from each selected type
```

### Examples

Generate a password containing 12 characters.
```bash
python3 genpw/genpw.py 12
```

Generate a larger password with no digits.
```bash
python3 genpw/genpw.py 20 --exclude digits
```

Generate a short password, but make sure it contains a character of each group: lowercase, uppercase, digits and symbols.
```bash
python3 genpw/genpw.py 5 --strict
```