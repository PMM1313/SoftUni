cards = input()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

card_list = cards.split()

for card in card_list:
    team = card[0]
    number = int(card[2:])

    if team == 'A':
        if number in team_a:
            team_a.remove(number)
            if len(team_a) < 7:
                print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
                print("Game was terminated")
                break
    elif team == 'B':
        if number in team_b:
            team_b.remove(number)
            if len(team_b) < 7:
                print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
                print("Game was terminated")
                break

# If the game is not terminated, print the final team sizes
else:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
