import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ',|\n'

        if numbers.startswith('//'):
            match = re.match(r"//(.+)\n(.*)", numbers)

            if match:
                delimiter = re.escape(match.group(1))
                numbers = match.group(2)

        numbers_arr = re.split(delimiter, numbers)

        return sum([int(number) for number in numbers_arr])