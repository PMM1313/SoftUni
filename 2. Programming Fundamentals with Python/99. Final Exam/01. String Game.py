def process_commands(s):
    list_with_changes = []

    while True:
        command = input().strip()
        if command == "Done":
            break

        if command.startswith("Change"):
            first_word, char, replacement = command.split()
            s = s.replace(char, replacement)
            list_with_changes.append(s)

        elif command.startswith("Includes"):
            first_word, substring = command.split(maxsplit=1)
            list_with_changes.append("True" if substring in s else "False")

        elif command.startswith("End"):
            first_word, substring = command.split(maxsplit=1)
            list_with_changes.append("True" if s.endswith(substring) else "False")

        elif command == "Uppercase":
            s = s.upper()
            list_with_changes.append(s)

        elif command.startswith("FindIndex"):
            first_word, char = command.split()
            index = s.find(char)
            list_with_changes.append(index)

        elif command.startswith("Cut"):
            first_word, startIndex, count = command.split()
            startIndex, count = int(startIndex), int(count)
            s = s[startIndex:startIndex + count]
            list_with_changes.append(s)

    return list_with_changes


initial_string = input().strip()

results = process_commands(initial_string)

for result in results:
    print(result)
