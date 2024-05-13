
is_current_bigger_than_n = False
current = 1
n = int(input())

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current > n:
            is_current_bigger_than_n = True
            break
        print(str(current) + ' ', end='')
        current += 1
    if is_current_bigger_than_n:
        break
    print()
    