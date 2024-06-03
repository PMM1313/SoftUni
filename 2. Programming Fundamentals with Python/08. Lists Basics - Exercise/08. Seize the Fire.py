fire_info = list(input().split("#"))
water_level = int(input())

effort = 0
total_fire = 0
extinguished_cells = []

for fire in fire_info:
    fire = fire.split(' = ')
    fire_type = fire[0]
    fire_strength = int(fire[1])

    # Check for High fire type
    if fire_type == 'High' and 81 <= fire_strength <= 125:
        if fire_strength <= water_level:
            water_level -= fire_strength
            total_fire += fire_strength
            effort += (fire_strength * 0.25)
            extinguished_cells.append(fire_strength)

    # Check for Medium fire type
    if fire_type == 'Medium' and 51 <= fire_strength <= 80:
        if fire_strength <= water_level:
            water_level -= fire_strength
            total_fire += fire_strength
            effort += (fire_strength * 0.25)
            extinguished_cells.append(fire_strength)

    # Check for Low fire type
    if fire_type == 'Low' and 1 <= fire_strength <= 50:
        if fire_strength <= water_level:
            water_level -= fire_strength
            total_fire += fire_strength
            effort += (fire_strength * 0.25)
            extinguished_cells.append(fire_strength)

# Print results
print(f'Cells:')
for number in extinguished_cells:
    print(f' - {number}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
