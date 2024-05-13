izbrano_chislo = int(input())

special_numbers = []

# Iterate through numbers from 1111 to 9999
for number in range(1111, 10000):
    digits = [int(digit) for digit in str(number)]

    # Check if every digit is not zero and divides the divisor without remainder
    if all(digit != 0 and izbrano_chislo % digit == 0 for digit in digits):
        special_numbers.append(number)

# Print the list of special numbers
print(*special_numbers)
