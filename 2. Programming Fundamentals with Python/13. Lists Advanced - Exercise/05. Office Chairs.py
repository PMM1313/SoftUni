def check_chairs(n, rooms):
    total_free_chairs = 0
    messages = []

    for room_number in range(1, n + 1):
        room_info = rooms[room_number - 1]
        chairs_info, num_visitors = room_info.rsplit(' ', 1)
        num_visitors = int(num_visitors)
        num_chairs = len(chairs_info)

        free_chairs = num_chairs - num_visitors

        if free_chairs >= 0:
            total_free_chairs += free_chairs
        else:
            needed_chairs = abs(free_chairs)
            messages.append(f"{needed_chairs} more chairs needed in room {room_number}")

    if messages:
        for message in messages:
            print(message)
    else:
        print(f"Game On, {total_free_chairs} free chairs left")

# Example usage:
n = int(input())
rooms = []
for i in range(n):
    room_info = input()
    rooms.append(room_info)

# Call the function with gathered inputs
check_chairs(n, rooms)