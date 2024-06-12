def min_max_sum(sequence):
    def convert_to_int_list(sequence):
        numbers_as_strings = sequence.split()
        numbers_as_integers = []
        for num_str in numbers_as_strings:
            num_int = int(num_str)
            numbers_as_integers.append(num_int)
        return numbers_as_integers

    numbers = convert_to_int_list(sequence)
    min_num = min(numbers)
    max_num = max(numbers)
    total_sum = sum(numbers)

    return min_num, max_num, total_sum


sequence = input()
min_num, max_num, total_sum = min_max_sum(sequence)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {total_sum}")