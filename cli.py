"""
cli.py - Interactive command-line interface for the calculator
"""

from calculator import calculate, square_root, OPERATIONS
from history import CalculationHistory


BANNER = r"""
  ╔══════════════════════════════════╗
  ║   Python Calculator  v1.0        ║
  ║   Type 'help' for commands       ║
  ╚══════════════════════════════════╝
"""

HELP_TEXT = """
  ┌─────────────────────────────────────────────────────┐
  │  USAGE                                              │
  │  Enter an expression:  <number> <op> <number>       │
  │  Examples:  5 + 3      12 / 4      2 ** 8           │
  │             sqrt 16    ans * 2  (use last result)   │
  │                                                     │
  │  OPERATORS                                          │
  │   +   Addition          -   Subtraction             │
  │   *   Multiplication    /   Division                │
  │   %   Modulo            **  Exponentiation          │
  │   sqrt <n>              Square root                 │
  │                                                     │
  │  COMMANDS                                           │
  │   history  – show calculation history               │
  │   clear    – clear history                          │
  │   help     – show this message                      │
  │   quit / exit / q – exit the calculator             │
  └─────────────────────────────────────────────────────┘
"""


def parse_number(token: str, ans) -> float:
    """Parse a token as a float, supporting 'ans' as the last result."""
    if token.lower() == "ans":
        if ans is None:
            raise ValueError("No previous answer available.")
        return float(ans)
    return float(token)


def run():
    history = CalculationHistory()
    ans = None  # Holds the last result

    print(BANNER)

    while True:
        try:
            raw = input("  calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye!")
            break

        if not raw:
            continue

        lower = raw.lower()

        # ── Commands ──────────────────────────────────────────
        if lower in ("quit", "exit", "q"):
            print("  Goodbye!")
            break

        if lower == "help":
            print(HELP_TEXT)
            continue

        if lower == "history":
            print()
            history.display()
            print()
            continue

        if lower == "clear":
            history.clear()
            print("  History cleared.")
            continue

        # ── sqrt shorthand ────────────────────────────────────
        tokens = raw.split()

        if tokens[0].lower() == "sqrt":
            if len(tokens) != 2:
                print("  Usage: sqrt <number>")
                continue
            try:
                n = parse_number(tokens[1], ans)
                result = square_root(n)
                ans = result
                expr = f"sqrt({n})"
                print(f"  = {result}")
                history.add(expr, result)
            except (ValueError, ZeroDivisionError) as exc:
                print(f"  Error: {exc}")
            continue

        # ── Binary expression: <a> <op> <b> ──────────────────
        if len(tokens) == 3:
            a_tok, op, b_tok = tokens
            try:
                a = parse_number(a_tok, ans)
                b = parse_number(b_tok, ans)
                result = calculate(a, op, b)
                ans = result
                expr = f"{a} {op} {b}"
                print(f"  = {result}")
                history.add(expr, result)
            except ZeroDivisionError as exc:
                print(f"  Math Error: {exc}")
            except ValueError as exc:
                print(f"  Input Error: {exc}")
            continue

        print("  Unrecognised input. Type 'help' for usage.")


if __name__ == "__main__":
    run()
