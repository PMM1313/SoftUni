
total_tournaments = int(input())
initial_points = int(input())
current_points = initial_points
won_tournaments = 0

for _ in range(total_tournaments):
    tournament_stage = input()

    if tournament_stage == "W":
        current_points += 2000
        won_tournaments += 1
    elif tournament_stage == "F":
        current_points += 1200
    elif tournament_stage == "SF":
        current_points += 720


point_without_initial = current_points - initial_points
average_points = point_without_initial // total_tournaments
percentage_won = (won_tournaments / total_tournaments) * 100


print(f"Final points: {current_points}")
print(f"Average points: {average_points}")
print(f"{percentage_won:.2f}%")
