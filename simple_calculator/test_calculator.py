# test_calculator.py

import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        assert calculator.add(3, 2) == 5

    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2

    def test_multiply(self):
        assert calculator.multiply(4, 2) == 8

    def test_divide(self):
        assert calculator.divide(10, 2) == 5

    def test_divide_by_zero(self):
        try:
            calculator.divide(10, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero!"

if __name__ == "__main__":
    unittest.main()