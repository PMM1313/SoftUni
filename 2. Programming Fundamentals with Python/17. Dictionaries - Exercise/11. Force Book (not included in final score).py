force_sides = {}
user_to_side = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        parts = command.split(" | ")
        force_side = parts[0]
        force_user = parts[1]

        if force_user not in user_to_side:
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)
            user_to_side[force_user] = force_side

    elif " -> " in command:
        parts = command.split(" -> ")
        force_user = parts[0]
        force_side = parts[1]

        if force_user in user_to_side:
            current_side = user_to_side[force_user]
            if current_side != force_side:
                force_sides[current_side].remove(force_user)
                if force_side not in force_sides:
                    force_sides[force_side] = []
                force_sides[force_side].append(force_user)
                user_to_side[force_user] = force_side
                print(force_user + " joins the " + force_side + " side!")
        else:
            if force_side not in force_sides:
                force_sides[force_side] = []
            force_sides[force_side].append(force_user)
            user_to_side[force_user] = force_side
            print(force_user + " joins the " + force_side + " side!")

for side in force_sides:
    if len(force_sides[side]) > 0:
        print("Side: " + side + ", Members: " + str(len(force_sides[side])))
        for user in force_sides[side]:
            print("! " + user)

