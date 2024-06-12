def sort_numbers(sequence):
    def convert_to_int_list(sequence):
        numbers_as_strings = sequence.split()
        numbers_as_integers = []
        for num_str in numbers_as_strings:
            num_int = int(num_str)
            numbers_as_integers.append(num_int)
        return numbers_as_integers

    numbers = convert_to_int_list(sequence)
    sorted_numbers = sorted(numbers)
    return sorted_numbers


sequence = input()
sorted_numbers = sort_numbers(sequence)
print(sorted_numbers)