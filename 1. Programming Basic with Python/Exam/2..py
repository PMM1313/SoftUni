import math

days = int(input())
food_left = int(input())
food_deer_1 = float(input())
food_deer_2 = float(input())
food_deer_3 = float(input())

# needed food
total_food_needed = days * (food_deer_1 + food_deer_2 + food_deer_3)

# check food supply
if total_food_needed <= food_left:
    print(f"{math.floor(food_left - total_food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed - food_left)} more kilos of food are needed.")
