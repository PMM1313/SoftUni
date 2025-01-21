n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "B":
            bunny = [row, col]

possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
