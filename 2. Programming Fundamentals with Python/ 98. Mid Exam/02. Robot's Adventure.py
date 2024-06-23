
grid = list(map(int, input().split('|')))

total_items = 0
command = ''

while command != "Adventure over":
    command = input()
    if command == "Adventure over":
        break

    if command.startswith("Step Backward$"):
        _, start_index, steps_str = command.split('$')
        start_index = int(start_index)
        steps = int(steps_str)

        if 0 <= start_index < len(grid):

            new_index = (start_index - steps) % len(grid)
            collected_items = grid[new_index]
            total_items += collected_items
            grid[new_index] = 0

    elif command.startswith("Step Forward$"):
        _, start_index, steps_str = command.split('$')
        start_index = int(start_index)
        steps = int(steps_str)

        if 0 <= start_index < len(grid):

            new_index = (start_index + steps) % len(grid)

            collected_items = grid[new_index]
            total_items += collected_items
            grid[new_index] = 0

    elif command.startswith("Double "):
        _, index_str = command.split()
        index = int(index_str)

        if 0 <= index < len(grid):
            grid[index] *= 2

    elif command == "Switch":
        grid.reverse()


print(" - ".join(map(str, grid)))
print(f"Robo finished the adventure with {total_items} items!")

