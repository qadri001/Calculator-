"""
test_calculator.py - Unit tests for core calculator functions
"""

import unittest
from calculator import add, subtract, multiply, divide, modulo, power, square_root, calculate


class TestBasicOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 999), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333, places=9)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(9, 3), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(5, 0), 1)

    def test_square_root(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)

    def test_square_root_negative(self):
        with self.assertRaises(ValueError):
            square_root(-1)


class TestCalculateDispatch(unittest.TestCase):

    def test_all_operators(self):
        self.assertEqual(calculate(8, '+', 2), 10)
        self.assertEqual(calculate(8, '-', 2), 6)
        self.assertEqual(calculate(8, '*', 2), 16)
        self.assertEqual(calculate(8, '/', 2), 4.0)
        self.assertEqual(calculate(8, '%', 3), 2)
        self.assertEqual(calculate(2, '**', 8), 256)

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, '&', 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
