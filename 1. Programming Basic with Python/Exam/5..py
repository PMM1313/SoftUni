player = ""
goals = 0
hat_trick = False

while True:
    player_name = input()

    if player_name == "END":
        break

    goals_scored = int(input())

    if goals_scored >= 10:
        goals = goals_scored
        player = player_name
        hat_trick = True
        break

    if goals_scored > goals:
        goals = goals_scored
        player = player_name
        if goals_scored >= 3:
            hat_trick = True
        else:
            hat_trick = False

print(f"{player} is the best player!")

if hat_trick:
    print(f"He has scored {goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals} goals.")
