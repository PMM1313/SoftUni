number = int(input())

stack = []
iterations = 0

while iterations < number:
    command = input()
    iterations += 1

    if command.startswith('1'):  # Push operation
        _, num = command.split()
        stack.append(int(num))

    elif command == '2':  # Pop operation
        if stack:
            stack.pop()

    elif command == '3':  # Print maximum
        if stack:
            print(max(stack))

    elif command == '4':  # Print minimum
        if stack:
            print(min(stack))

# Print stack from top to bottom in the required format
print(", ".join(map(str, reversed(stack))))
