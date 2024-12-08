class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        numbers = numbers.replace('\n', ',')
        numbers_arr = numbers.split(",")

        return sum([int(number) for number in numbers_arr])