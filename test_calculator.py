import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(1, 0)