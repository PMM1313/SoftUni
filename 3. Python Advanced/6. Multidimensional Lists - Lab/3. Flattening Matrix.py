
number_of_lines = int(input())

matrix = []
for _ in range(number_of_lines):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

result = []

for row in matrix:
    for el in row:
        result.append(el)

print(result)