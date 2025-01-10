number = int(input())

stack = []
iterations = 0

functions = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack) if stack else None),
    "4": lambda: print(min(stack) if stack else None)
}


while iterations < number:

    command = input()
    functions[command[0]](*command[1:])

# Print stack from top to bottom in the required format
print(*reversed(stack), sep=", ")

