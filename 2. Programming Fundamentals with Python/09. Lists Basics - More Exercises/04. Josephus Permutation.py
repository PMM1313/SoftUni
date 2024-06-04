
circle = list(map(int, input().split()))
step = int(input())

result = []
index = 0

while circle:

    index = (index + step - 1) % len(circle)

    result.append(circle.pop(index))


print(f"[{','.join(map(str, result))}]")
