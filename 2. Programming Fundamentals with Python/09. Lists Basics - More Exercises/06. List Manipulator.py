# Read initial list
lst = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    command_parts = command.split()
    cmd_type = command_parts[0]

    if cmd_type == "exchange":
        index = int(command_parts[1])
        if 0 <= index < len(lst):
            lst = lst[index + 1:] + lst[:index + 1]
        else:
            print("Invalid index")
    elif cmd_type == "max":
        parity = command_parts[1]
        if parity == "even":
            numbers = [num for num in lst if num % 2 == 0]
        else:
            numbers = [num for num in lst if num % 2 != 0]

        if not numbers:
            print("No matches")
        else:
            max_num = max(numbers)
            max_index = len(lst) - 1 - lst[::-1].index(max_num)
            print(max_index)
    elif cmd_type == "min":
        parity = command_parts[1]
        if parity == "even":
            numbers = [num for num in lst if num % 2 == 0]
        else:
            numbers = [num for num in lst if num % 2 != 0]

        if not numbers:
            print("No matches")
        else:
            min_num = min(numbers)
            min_index = len(lst) - 1 - lst[::-1].index(min_num)
            print(min_index)
    elif cmd_type == "first":
        count = int(command_parts[1])
        parity = command_parts[2]
        if count > len(lst):
            print("Invalid count")
        else:
            if parity == "even":
                numbers = [num for num in lst if num % 2 == 0]
            else:
                numbers = [num for num in lst if num % 2 != 0]

            print(numbers[:count])
    elif cmd_type == "last":
        count = int(command_parts[1])
        parity = command_parts[2]
        if count > len(lst):
            print("Invalid count")
        else:
            if parity == "even":
                numbers = [num for num in lst if num % 2 == 0]
            else:
                numbers = [num for num in lst if num % 2 != 0]

            print(numbers[-count:])

# Print the final state of the list
print(f"[{', '.join(map(str, lst))}]")
