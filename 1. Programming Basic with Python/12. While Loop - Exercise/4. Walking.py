
steps_count_total = 0
goal = 10000
steps_count = 0


while steps_count_total < goal:
    steps_count = input()

    if steps_count == 'Going home':
        steps_home = int(input())
        steps_count_total += steps_home
        break

    steps_count_total += int(steps_count)


if steps_count_total >= goal:
    print(f'Goal reached! Good job!')
    print(f'{steps_count_total - goal} steps over the goal!')
elif steps_count_total < goal:
    print(f'{goal - steps_count_total} more steps to reach goal.')



