def odd_and_even_sum(number: int) -> str:

    odd_sum = 0
    even_sum = 0

    for digit in str(number):
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


# Take input from the user
input_number = int(input())
result = odd_and_even_sum(input_number)
print(result)