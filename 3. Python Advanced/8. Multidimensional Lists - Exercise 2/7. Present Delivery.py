presents = int(input())
n = int(input())

matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1



directions = {"up": (-1, 0),
              "down": (1, 0),
              "left": (0, -1),
              "right": (0, 1)}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    r, c = (santa[0] + directions[command][0],
            santa[1] + directions[command][1])
    if 0 <= n and 0 <= c < n:
        if matrix[r][c] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[r][c] = "-"  # Mark the gifted present
