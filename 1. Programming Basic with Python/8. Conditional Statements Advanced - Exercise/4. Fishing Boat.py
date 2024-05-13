
budget = int(input())
season = str(input())
number_of_workers = int(input())

discount_for_people = 0
season_fee = 0

# discount if even, but without Autumn
discount_for_even = 1

# prices for ship in season
FEE_FOR_SHIP_SPRING = 3000
FEE_FOR_SHIP_SUMMER = 4200
FEE_FOR_SHIP_AUTUMN = 4200
FEE_FOR_SHIP_WINTER = 2600


if season == 'Spring':
    season_fee = 3000
elif season == 'Summer':
    season_fee = 4200
elif season == 'Autumn':
    season_fee = 4200
elif season == 'Winter':
    season_fee = 2600

# discount for NUMBER of people:
if number_of_workers <= 6:
    discount_for_people = 0.90
elif 7 <= number_of_workers <= 11:
    discount_for_people = 0.85
elif number_of_workers > 12:
    discount_for_people = 0.75

if number_of_workers % 2 == 0 and season != 'Autumn':
    discount_for_even = 0.95

total_sum = (season_fee * discount_for_people) * discount_for_even

if total_sum <= budget:
    money_left = budget - total_sum
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = total_sum - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
