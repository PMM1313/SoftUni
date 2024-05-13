
price_of_holiday = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddy_bear = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

# Prices:
price_of_puzzle = 2.60
price_of_doll = 3.00
price_of_teddy_bear = 4.10
price_of_minions = 8.20
price_of_truck = 2.00

# calculating all the toys as sum:
total_puzzle_cost = number_of_puzzles * price_of_puzzle
total_doll_cost = number_of_dolls * price_of_doll
total_teddy_bear_cost = number_of_teddy_bear * price_of_teddy_bear
total_minions_cost = number_of_minions * price_of_minions
total_truck_cost = number_of_trucks * price_of_truck

all_the_toys = total_puzzle_cost + total_doll_cost + total_teddy_bear_cost + total_minions_cost + total_truck_cost

# calculating NUMBER of toys:
number_of_toys = number_of_puzzles + number_of_dolls + number_of_teddy_bear + number_of_minions + number_of_trucks

# if over 50 toys.
if number_of_toys >= 50:
    discount = all_the_toys*0.25
    all_the_toys -= discount

# 10% from profit for rent
rent_as_percentage = 0.10   # 10%
rent = all_the_toys * rent_as_percentage
profit = all_the_toys - rent

if profit >= price_of_holiday:
    leftover = profit - price_of_holiday
    print(f'Yes! {leftover:.2f} lv left.')
else:
    needed_money = price_of_holiday - profit
    print(f'Not enough money! {needed_money:.2f} lv needed.')
