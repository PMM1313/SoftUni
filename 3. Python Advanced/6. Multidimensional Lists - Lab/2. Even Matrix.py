rows_count = int(input())

matrix = []

for _ in range(rows_count):
    row_data = [int(el) for el in input().split(", ")]
    matrix.append(row_data)

result = []

for row_index in range(len(matrix)):
    result.append([])
    for el in matrix[row_index]:
        if el % 2 == 0:  # Check if the number is even
            result[row_index].append(el)

print(result)