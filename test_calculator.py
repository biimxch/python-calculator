import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Test cases for add()
    def test_add_positive(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Test cases for subtract()
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_with_negative_result(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # Test cases for multiply()
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # Test cases for divide()
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_divide_by_one(self):
        self.assertEqual(self.calc.divide(10, 1), 10)

    # Test cases for modulo()
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_when_divisible(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

if __name__ == '__main__':
    unittest.main()
