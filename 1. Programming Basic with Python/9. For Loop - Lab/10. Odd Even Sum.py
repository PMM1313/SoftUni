n = int(input())
even_sum = 0
odd_sum = 0


for i in range(n):
    number = int(input())
    if i % 2 == 0:                 # Четна позиция
        even_sum += number
    else:                          # Нечетна позиция
        odd_sum += number


difference = abs(even_sum - odd_sum)


if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {difference}')
