
n = int(input())

for _ in range(n):
    numbers = int(input())

    if numbers % 2 != 0:
        print(f'{numbers} is odd!')
        break
else:
    print('All numbers are even.')
