def group_numbers(numbers_str):
    numbers = list(map(int, numbers_str.split(", ")))
    group_boundary = 10

    while numbers:
        group_numbers = [num for num in numbers if num <= group_boundary]
        if group_numbers:
            print(f"Group of {group_boundary}'s: {group_numbers}")
        else:
            print(f"Group of {group_boundary}'s: []")
        numbers = [num for num in numbers if num > group_boundary]
        group_boundary += 10

# Example usage:
numbers_str = input()
group_numbers(numbers_str)