
number = int(input())

stack = []
iterations = 0

while iterations <= number:
    
    iterations += 1
    command = input()

    if '1' in command:
        list = command.split()
        number = int(list[1])
        stack.append(number)

    elif '2' in command:
        stack.pop()

    elif '3' in command:
        max_number = max(stack)
        print(max_number)

    elif '4' in command:
        min_number = min(stack)
        print(min_number)

while stack:
    print(stack.pop(), end=' ')
