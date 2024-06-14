def classify_numbers(numbers):
    # Split the input string into a list of numbers
    numbers_list = numbers.split(", ")

    # Convert the list of strings to a list of integers
    numbers_list = list(map(int, numbers_list))

    # Initialize empty lists for classification
    positive = []
    negative = []
    even = []
    odd = []

    # Classify numbers based on their properties
    for num in numbers_list:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    # Print the results
    print(f"Positive: {', '.join(map(str, positive))}")
    print(f"Negative: {', '.join(map(str, negative))}")
    print(f"Even: {', '.join(map(str, even))}")
    print(f"Odd: {', '.join(map(str, odd))}")

# Example usage:
string = input()
classify_numbers(string)
