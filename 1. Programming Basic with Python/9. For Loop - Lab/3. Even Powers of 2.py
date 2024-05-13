n = int(input())

for i in range(n + 1):
    result = 2 ** i
    if i % 2 == 0:
        print(result)
