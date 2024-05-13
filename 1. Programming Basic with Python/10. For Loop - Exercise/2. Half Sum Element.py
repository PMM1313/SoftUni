
n = int(input())

max_number = float('-inf')

total_sum = 0

# Четем number_of_models числа и ги сумираме
for i in range(n):
    number = int(input())
    total_sum += number
    if number > max_number:
        max_number = number


difference = abs(max_number - (total_sum - max_number))


if max_number == total_sum - max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {difference}')
