import unittest
from calculator import StringCalculator

class StringCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)
    
    def test_one_number_string(self):
        self.assertEqual(self.calculator.add("1"), 1)
    
    def test_two_number_string(self):
        self.assertEqual(self.calculator.add("1, 2"), 3)

    def test_multiple_number_string(self):
        self.assertEqual(self.calculator.add("1, 2, 3, 4, 5"), 15)

    def test_new_lines_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)
    
    def test_different_delimiters_1(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)
    
    def test_different_delimiters_2(self):
        self.assertEqual(self.calculator.add("//|\n4|5|6"), 15)

if __name__ == '__main__':
    unittest.main()
