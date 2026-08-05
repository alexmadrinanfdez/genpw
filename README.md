# genpw

A command-line tool to generate secure, random passwords based on user requirements.

## Usage

Run the script from the root folder of the repository:

```bash
python3 -m genpw.genpw [options]
```

### Options

Use with the `--help` option to view the command documentation.

| Option | Short version | Description | Default |
| --- | --- | --- | --- |
| `length` | | Number of characters in the generated password. | 10 |
| `--help` | `-h`| Show help message and exit. |  |
| `--exclude` | `-e`| Space-separated list of character types to exclude from the password. Valid values are `lower`, `upper`, `digits` and `punctuation`. | None |
| `--strict` | `-s`| Enforce at least one character from each included type. | Off |

Note that the fact that no character types are excluded by default means they are all included unless specified.

### Examples

Generate a password containing 12 characters.
```bash
python3 -m genpw.genpw 12
```

Generate a larger password with no digits.
```bash
python3 -m genpw.genpw 20 --exclude digits
```

Generate a short password, but make sure it contains a character of each group: lowercase, uppercase, digits and punctuation symbols.
```bash
python3 -m genpw.genpw 5 --strict
```