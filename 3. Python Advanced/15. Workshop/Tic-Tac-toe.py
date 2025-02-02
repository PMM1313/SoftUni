class InvalidPositionNumber(Exception):
    pass
class PositionAlreadyTaken(Exception):
    pass

def obtain_valid_position(player, matrix):
    while True:
        try:
            selected_position = int(input(f"{player}, please select a position"))
            if selected_position < 1 or selected_position > 9:
                raise InvalidPositionNumber

            row, col = position_mapper[selected_position]
            if matrix[row][col] != '':
                raise PositionAlreadyTaken
            return selected_position
        except ValueError:
            print("Please select a number between 1-9")
        except InvalidPositionNumber:
            print("Please enter position number")
        except PositionAlreadyTaken:
            print("Position taken")

player1_name = input("Player 1, enter your name")
player2_name = input("Player 2, enter your name")

symbol = input()
while True:

    if symbol not in ["X", "x", "O", "o"]:
        symbol = input()
    else:
        break

player1_symbol = symbol.upper()
player2_symbol = "O" if player1_symbol == "X" else "X"

position_matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in position_matrix:
    print("|".join([str(cell) if cell!=0 else " " for cell in row]))

print(f"{player1_name} starts first")

position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)

}
matrix = [['','', ''], ['','', ''], ['','', '']]

player_to_symbol = {
    player1_name: player1_symbol,
    player2_name: player2_symbol,
}
def is_winner(player_symbol, matrix):
    matrix_length = len(matrix)
    for row in matrix:
        if all([el == player_symbol for el in row]):
            return True

    for col_index in range(matrix_length):
        if all([matrix[row_index][col_index] == player_symbol for row_index in range(matrix_length)]):
            return True

    main_diagonal_winner = [matrix[index][index] == player_symbol for index in range(matrix_length)]
    diagonal_winner = all([matrix[matrix_length - 1 - col_index][col_index] == player_to_symbol for col_index in range(matrix_length - 1)])

    if main_diagonal_winner or diagonal_winner:

        return True
    return False

def print_board(board):
    for row in board:
        print(f"|  {'  |  '.join(row)}  |")

def play_turn(player_symbol, row, col, matrix, turns_count):
    matrix[row][col] = player_symbol

    if turns_count >= 5:
        is_winner(player_symbol, matrix)
    print_board(matrix)
turns_count = 1
while True:
    current_player_name = player2_name if turns_count %2 == 0 else player1_name
    position = obtain_valid_position(current_player_name, matrix)
    row, col = position_mapper[position]
    player_symbol = player_to_symbol[current_player_name]
    winner = play_turn(player_symbol, row, col, matrix, turns_count)

    if winner:
        print("You Won!")
        break

    turns_count += 1

    if turns_count == 10:
        print("No winner - game over")
        break
