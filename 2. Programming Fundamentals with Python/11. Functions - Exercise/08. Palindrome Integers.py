def check_palindrome_integers(sequence):
    def is_palindrome(number):
        return str(number) == str(number)[::-1]

    integers = sequence.split(", ")
    palindrome_results = []
    for num_str in integers:
        num = int(num_str)
        palindrome_results.append(is_palindrome(num))
    return palindrome_results


sequence = input()
palindrome_results = check_palindrome_integers(sequence)
for result in palindrome_results:
    print(result)