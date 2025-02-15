def process_data(size, grid, commands):
    pacman_row, pacman_column = 0, 0
    total_stars = 0
    health = 100
    collected_stars = 0
    immune = False
    directions = \
        {"up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),}

    for row in range(size):
        for column in range(size):
            if grid[row][column] == "P":
                pacman_row, pacman_column = row, column
            elif grid[row][column] == "*":
                total_stars += 1

    grid[pacman_row][pacman_column] = "-"

    for command in commands:
        if command == "end":
            break

        move_r, move_c = directions[command]
        new_row = (pacman_row + move_r) % size
        new_column = (pacman_column + move_c) % size
        cell = grid[new_row][new_column]

        if cell == "*":
            collected_stars += 1

        elif cell == "G":
            if immune:
                immune = False
            else:
                health -= 50
                if health <= 0:
                    pacman_row, pacman_column = new_row, new_column
                    print(f"Game over! Pacman last coordinates [{pacman_row},{pacman_column}]")
                    print(f"Health: {health}")
                    if total_stars - collected_stars > 0:
                        print(f"Uncollected stars: {total_stars - collected_stars}")
                    grid[pacman_row][pacman_column] = "P"
                    [print("".join(row)) for row in grid]
                    return
        elif cell == "F":
            immune = True

        pacman_row, pacman_column = new_row, new_column
        grid[pacman_row][pacman_column] = "-"

        if collected_stars == total_stars:
            print("Pacman wins! All the stars are collected.")
            print(f"Health: {health}")
            grid[pacman_row][pacman_column] = "P"
            [print("".join(row)) for row in grid]
            return

    print("Pacman failed to collect all the stars.")
    print(f"Health: {health}")
    if total_stars - collected_stars > 0:
        print(f"Uncollected stars: {total_stars - collected_stars}")
        # print(f"Collected stars: {collected_stars}")
        # print(f"Total stars: {total_stars}")
    grid[pacman_row][pacman_column] = "P"
    [print("".join(row)) for row in grid]



map_size = int(input())
grid = [list(input()) for _ in range(map_size)]
commands = []

while True:
    cmd = input()

    if cmd == "end":
        commands.append(cmd)
        break
    commands.append(cmd)

process_data(map_size, grid, commands)
