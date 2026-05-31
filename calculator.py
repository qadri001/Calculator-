"""
calculator.py - Core calculator logic with full arithmetic operations
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulo(a, b):
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return a % b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def square_root(a):
    """Return the square root of a."""
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return a ** 0.5


OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulo,
    '**': power,
}


def calculate(a, operator, b):
    """
    Perform a calculation given two operands and an operator string.
    Supports: +, -, *, /, %, **
    """
    if operator not in OPERATIONS:
        raise ValueError(f"Unsupported operator: '{operator}'. "
                         f"Supported: {list(OPERATIONS.keys())}")
    return OPERATIONS[operator](a, b)
