n = int(input())

matrix = []
for _ in range(n):
    row_data = list(input())
    matrix.append(row_data)

searched_symbols = input()

for row_index in range(len(matrix)):
    for col_index in range (len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_symbols:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searched_symbols} does not occur in the matrix")



