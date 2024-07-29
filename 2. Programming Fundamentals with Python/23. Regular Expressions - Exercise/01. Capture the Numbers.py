import re
import sys


def extract_numbers_from_lines():
    numbers = []

    # Read input from standard input (sys.stdin)
    input_lines = sys.stdin.read().splitlines()

    for line in input_lines:
        # Use regex to find all sequences of digits
        found_numbers = re.findall(r'\d+', line)
        numbers.extend(found_numbers)

    # Print all extracted numbers separated by a space
    print(' '.join(numbers))


if __name__ == "__main__":
    extract_numbers_from_lines()
