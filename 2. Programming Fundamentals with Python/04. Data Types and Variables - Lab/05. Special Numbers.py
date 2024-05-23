number = int(input())

for num in range(1, number + 1):
    # Calculate the sum of the digits manually
    sum_of_digits = 0
    for digit in str(num):
        sum_of_digits += int(digit)

    sum_of_digits = sum(int(digit) for digit in str(num))

    special = sum_of_digits in {5, 7, 11}

    print(f"{num} -> {special}")
