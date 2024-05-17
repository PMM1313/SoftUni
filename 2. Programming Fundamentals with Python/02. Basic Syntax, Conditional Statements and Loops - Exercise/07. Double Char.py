
while True:
    command = str(input())

    if command == 'End':
        break
    elif command == 'SoftUni':
        continue

    doubled_string = ''

    for char in command:
        doubled_string += char * 2

    print(doubled_string)
