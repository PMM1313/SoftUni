import math

number_of_days = int(input())
food_for_animals = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

grams_to_kilos_ratio = 1000
turtle_food_per_day_in_kilos = turtle_food_per_day / grams_to_kilos_ratio

# food left per animal total

total_dog_food = number_of_days * dog_food_per_day
total_cat_food = number_of_days * cat_food_per_day
total_turtle_food = number_of_days * turtle_food_per_day_in_kilos

total_food = total_turtle_food + total_cat_food + total_dog_food

if total_food <= food_for_animals:
    food_left = food_for_animals - total_food
    food_left_rounded = math.floor(food_left)
    print(f'{food_left_rounded} kilos of food left.')
else:
    food_needed = total_food - food_for_animals
    food_needed_rounded = math.ceil(food_needed)
    print(f'{food_needed_rounded} more kilos of food are needed.')
