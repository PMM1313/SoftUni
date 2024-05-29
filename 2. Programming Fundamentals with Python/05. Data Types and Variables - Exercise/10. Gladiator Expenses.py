lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_brakes = 0
total_repairs = 0

for fight in range(1, lost_fights + 1):

    if fight % 2 == 0:
        total_repairs += helmet_price

    if fight % 3 == 0:
        total_repairs += sword_price

    if fight % 2 == 0 and fight % 3 == 0:
        shield_brakes += 1
        total_repairs += shield_price

        if shield_brakes % 2 == 0:
            total_repairs += armor_price

print(f'Gladiator expenses: {total_repairs:.2f} aureus')
