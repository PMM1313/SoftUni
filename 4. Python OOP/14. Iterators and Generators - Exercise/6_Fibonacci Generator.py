def fibonacci():
    current_number, next_num = 0, 1
    while True:
        yield current_number
        current_number, next_num = next_num, current_number + next_num