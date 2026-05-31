# 🧮 Python Calculator

A clean, modular command-line calculator built in Python.

## Project Structure

```
calculator/
├── calculator.py       # Core arithmetic functions
├── cli.py              # Interactive command-line interface
├── history.py          # Calculation history (saved to history.json)
├── test_calculator.py  # Unit tests
└── README.md
```

## Getting Started

**Requirements:** Python 3.7+

### Run the interactive calculator

```bash
python cli.py
```

### Run the unit tests

```bash
python -m pytest test_calculator.py -v
# or without pytest:
python test_calculator.py
```

## Usage

Once the CLI is running, type expressions at the `calc>` prompt:

| Input          | Description               | Result  |
|----------------|---------------------------|---------|
| `5 + 3`        | Addition                  | `8`     |
| `10 - 4`       | Subtraction               | `6`     |
| `6 * 7`        | Multiplication            | `42`    |
| `15 / 4`       | Division                  | `3.75`  |
| `17 % 5`       | Modulo (remainder)        | `2`     |
| `2 ** 10`      | Exponentiation            | `1024`  |
| `sqrt 144`     | Square root               | `12.0`  |
| `ans + 1`      | Use last result           | —       |

### Commands

| Command   | Action                     |
|-----------|----------------------------|
| `history` | Show past calculations     |
| `clear`   | Clear history              |
| `help`    | Show usage guide           |
| `quit`    | Exit the calculator        |

## Features

- ✅ Basic arithmetic: `+`, `-`, `*`, `/`
- ✅ Advanced: modulo `%`, exponentiation `**`, `sqrt`
- ✅ `ans` keyword to reference the last result
- ✅ Persistent history saved to `history.json`
- ✅ Full unit test suite
- ✅ Graceful error handling (division by zero, invalid input, etc.)
