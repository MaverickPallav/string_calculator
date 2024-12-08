import unittest
from calculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):
    def test_empty_string(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add(""), 0)

if __name__ == '__main__':
    unittest.main()
