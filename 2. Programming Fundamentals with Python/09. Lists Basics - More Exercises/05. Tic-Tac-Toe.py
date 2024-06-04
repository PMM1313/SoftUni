# Read the input for the Tic-Tac-Toe field
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

# Combine the rows into a single 2D list to represent the field
field = [row1, row2, row3]

# Initialize winner to 0 (no winner)
winner = 0

# Check rows for a win
for row in field:
    if row[0] == row[1] == row[2] and row[0] != 0:
        winner = row[0]

# Check columns for a win
for col in range(3):
    if field[0][col] == field[1][col] == field[2][col] and field[0][col] != 0:
        winner = field[0][col]

# Check diagonals for a win
if field[0][0] == field[1][1] == field[2][2] and field[0][0] != 0:
    winner = field[0][0]
if field[0][2] == field[1][1] == field[2][0] and field[0][2] != 0:
    winner = field[0][2]

# Determine and print the result
if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
