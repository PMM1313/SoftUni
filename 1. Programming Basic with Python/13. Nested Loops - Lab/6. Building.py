
max_floors = int(input())
max_rooms = int(input())

for floor in range(max_floors, 0, -1):
    floor_string = ""
    for room in range(max_rooms):
        if floor == max_floors:
            floor_string += f"L{floor}{room} "
        elif floor % 2 == 0:
            floor_string += f"O{floor}{room} "
        else:
            floor_string += f"A{floor}{room} "
    print(floor_string)
