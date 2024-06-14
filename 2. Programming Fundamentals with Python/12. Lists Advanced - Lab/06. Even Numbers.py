def find_even_indices():

    numbers = input().split(", ")


    numbers = list(map(int, numbers))


    even_indices = [index for index, num in enumerate(numbers) if num % 2 == 0]


    print(even_indices)


# Example usage:
find_even_indices()