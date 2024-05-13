
actor_name = input()
academy_points = float(input())
evaluators_count = int(input())

total_points = academy_points

for _ in range(evaluators_count):
    evaluator_name = input()
    evaluator_points = float(input())

    total_points += len(evaluator_name) * evaluator_points / 2

    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
