def process_commands(s):
    output = []

    while True:
        command = input().strip()
        if command == "Done":
            break

        if command.startswith("Change"):
            first_word, char, replacement = command.split()
            s = s.replace(char, replacement)
            output.append(s)

        elif command.startswith("Includes"):
            first_word, substring = command.split(maxsplit=1)
            output.append("True" if substring in s else "False")

        elif command.startswith("End"):
            first_word, substring = command.split(maxsplit=1)
            output.append("True" if s.endswith(substring) else "False")

        elif command == "Uppercase":
            s = s.upper()
            output.append(s)

        elif command.startswith("FindIndex"):
            first_word, char = command.split()
            index = s.find(char)
            output.append(index)

        elif command.startswith("Cut"):
            first_word, startIndex, count = command.split()
            startIndex, count = int(startIndex), int(count)
            s = s[startIndex:startIndex + count]
            output.append(s)

    return output


# Read initial string
initial_string = input().strip()

# Process commands
results = process_commands(initial_string)

# Print results
for result in results:
    print(result)
