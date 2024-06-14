def todo_list():
    notes = []

    while True:
        command = input()

        if command == "End":
            break

        importance, note = command.split("-", 1)
        importance = int(importance)

        # Insert the note at the correct position based on its importance
        notes.append((importance, note))

    # Sort the notes based on the importance value
    notes.sort()

    # Extract the sorted notes without their importance values
    sorted_notes = [note for _, note in notes]

    print(sorted_notes)


# Example usage:
todo_list()