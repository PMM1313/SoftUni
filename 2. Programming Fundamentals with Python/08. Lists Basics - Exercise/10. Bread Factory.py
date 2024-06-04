work_day_event = input()

coins = 100
energy = 100

day_completed = True

work_day_event = work_day_event.split('|')

for event in work_day_event:
    event_or_ingredient = event.split('-')[0]
    number = int(event.split('-')[1])

    if event_or_ingredient == 'rest':

        if 100 <= energy + number:
            energy_gained = 100 - energy
            energy = 100
            print(f'You gained {energy_gained} energy.')
            print(f'Current energy: {energy}.')
        else:
            energy += number
            energy_gained = number
            print(f'You gained {energy_gained} energy.')
            print(f'Current energy: {energy}.')

    elif event_or_ingredient == 'order':

        if energy >= 30:
            energy -= 30
            coins_earned = number
            coins += coins_earned
            print(f'You earned {coins_earned} coins.')
        else:
            energy += 50
            print(f'You had to rest!')

    else:
        ingredient = event_or_ingredient
        cost = number
        if cost <= coins:
            coins -= cost
            print(f'You bought {ingredient}.')
        else:
            print(f'Closed! Cannot afford {ingredient}.')
            day_completed = False
            break

if day_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
