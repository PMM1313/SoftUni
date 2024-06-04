
numbers = list(map(int, input().split(", ")))

result = []
zeroes_count = 0

for number in numbers:
    if number == 0:
        zeroes_count += 1
    else:
        result.append(number)

result.extend([0] * zeroes_count)

print(result)
