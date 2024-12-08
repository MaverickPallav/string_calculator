import unittest
from calculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):
    def test_empty_string(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add(""), 0)
    
    def test_one_number_string(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1"), 1)
    
    def test_two_number_string(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.add("1, 2"), 3)

if __name__ == '__main__':
    unittest.main()
