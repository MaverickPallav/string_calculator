# String Calculator

A simple String Calculator built using Test Driven Development (TDD) in Python. It supports various input formats and behaviors, including custom delimiters, multiple numbers, and handling negative numbers.

## Features

- **Empty String**: Returns 0 for an empty string.
- **Single/Multiple Numbers**: Adds numbers in the string (e.g., `"1,2,3"` returns `6`).
- **Newlines**: Supports numbers separated by newlines (e.g., `"1\n2,3"`).
- **Custom Delimiters**: Supports custom delimiters (e.g., `"//;\n1;2"`).
- **Negative Numbers**: Throws an exception with negative numbers.
- **Large Numbers**: Ignores numbers greater than 1000.
- **Multiple Delimiters**: Supports multiple delimiters (e.g., `"//[*][%]\n1*2%3"`).
- **Any Length Delimiter**: Supports delimiter of any length (e.g., `"//[***]\n1***2***3"`).

## Installation

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/MaverickPallav/string_calculator.git
cd string_calculator
```

## Usage

```bash
python calculator_test.py OR python3 calculator_test.py
```
