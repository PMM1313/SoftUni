

def filter_even_numbers(numbers: str) -> list:
    def is_even(number: int) -> bool:
        return number % 2 == 0

    # Convert the string to a list of integers
    num_list = map(int, numbers.split())

    # Use filter to get even numbers
    even_numbers = list(filter(is_even, num_list))

    return even_numbers



input_numbers = input()
result = filter_even_numbers(input_numbers)
print(result)