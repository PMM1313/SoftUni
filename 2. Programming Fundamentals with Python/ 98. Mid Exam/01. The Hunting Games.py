
number_of_days = int(input())
people = int(input())
starting_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())

# Read energy losses for each day
energy_losses = []
for day in range(number_of_days):
    energy_losses.append(float(input()))

# Calculate total water and food
total_water = number_of_days * people * water_per_day
total_food = number_of_days * people * food_per_day

current_energy = starting_energy
current_water = total_water
current_food = total_food

for day in range(1, number_of_days + 1):
    energy_loss = energy_losses[day - 1]
    current_energy -= energy_loss

    if current_energy <= 0:
        print(
            f"You will run out of energy. You will be left with {current_food:.2f} food and {current_water:.2f} water.")
        break

    if day % 2 == 0:
        current_energy += 0.05 * current_energy
        current_water -= 0.30 * current_water

    if day % 3 == 0:
        current_energy += 0.10 * current_energy
        current_food -= current_food / people
else:
    print(f"You are ready for the quest. You will be left with - {current_energy:.2f} energy!")