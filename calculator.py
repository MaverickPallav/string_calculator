import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ',|\n'

        if numbers.startswith('//'):
            delimiter = self.get_custom_delimeter(numbers)
            numbers = numbers.split('\n', 1)[1]

        numbers_arr = re.split(delimiter, numbers)

        negative_numbers_arr = [int(number) for number in numbers_arr if int(number) < 0]

        if negative_numbers_arr:
            raise ValueError(f"Negatives not allowed: {negative_numbers_arr}")

        return sum([int(number) for number in numbers_arr if 0 <= int(number) <= 1000])

    def get_custom_delimeter(self, numbers):
        # For multiple delimiters
        match = re.match(r"//\[(.+)\]\n(.*)", numbers)
        if match:
            delimiters = re.split(r"\]\[", match.group(1))
            delimiter = '|'.join(map(re.escape, delimiters))
            return delimiter

        # For single delimiter
        match = re.match(r"//(.)\n(.*)", numbers)
        if match:
            delimiter = re.escape(match.group(1))
            return delimiter
        
        return ',|\n'