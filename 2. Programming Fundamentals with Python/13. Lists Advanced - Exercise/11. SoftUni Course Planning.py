def process_schedule(initial_lessons, commands):
    lessons = initial_lessons.split(", ")

    def add_lesson(lesson_title):
        if lesson_title not in lessons:
            lessons.append(lesson_title)

    def insert_lesson(lesson_title, index_to_insert):
        if lesson_title not in lessons:
            if 0 <= index_to_insert < len(lessons):
                lessons.insert(index_to_insert, lesson_title)

    def remove_lesson(lesson_title):
        exercise_title = lesson_title + "-Exercise"
        if lesson_title in lessons:
            lessons.remove(lesson_title)
        if exercise_title in lessons:
            lessons.remove(exercise_title)

    def swap_lessons(lesson_title1, lesson_title2):
        if lesson_title1 in lessons and lesson_title2 in lessons:
            index1 = lessons.index(lesson_title1)
            index2 = lessons.index(lesson_title2)
            lessons[index1], lessons[index2] = lessons[index2], lessons[index1]

            exercise1 = lesson_title1 + "-Exercise"
            exercise2 = lesson_title2 + "-Exercise"

            if exercise1 in lessons:
                lessons.remove(exercise1)
                if index2 + 1 <= len(lessons):
                    lessons.insert(index2 + 1, exercise1)
                else:
                    lessons.append(exercise1)
            elif exercise2 in lessons:
                lessons.remove(exercise2)
                if index1 + 1 <= len(lessons):
                    lessons.insert(index1 + 1, exercise2)
                else:
                    lessons.append(exercise2)

    def add_or_replace_exercise(lesson_title):
        exercise_title = lesson_title + "-Exercise"
        if lesson_title in lessons and exercise_title not in lessons:
            index = lessons.index(lesson_title)
            if index + 1 < len(lessons):
                lessons.insert(index + 1, exercise_title)
            else:
                lessons.append(exercise_title)
        elif lesson_title not in lessons:
            lessons.append(lesson_title)
            lessons.append(exercise_title)

    command_functions = {
        "Add": lambda args: add_lesson(args[0]),
        "Insert": lambda args: insert_lesson(args[0], int(args[1])),
        "Remove": lambda args: remove_lesson(args[0]),
        "Swap": lambda args: swap_lessons(args[0], args[1]),
        "Exercise": lambda args: add_or_replace_exercise(args[0])
    }

    for command in commands:
        command_parts = command.split(":")
        action = command_parts[0]
        args = command_parts[1:]

        if action in command_functions:
            command_functions[action](args)

    return lessons

# Read initial schedule from console input
initial_schedule = input().strip()

# Read commands until "course start" from console input
commands = []
while True:
    command = input().strip()
    if command == "course start":
        break
    commands.append(command)

# Process schedule
final_schedule = process_schedule(initial_schedule, commands)

# Output the final schedule
for i, lesson in enumerate(final_schedule, start=1):
    print(f"{i}.{lesson}")