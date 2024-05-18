budget = float(input())
price_of_kg_flour = float(input())

current_check = 0
bred_count = 0
eggs_count = 0

price_of_eggs = price_of_kg_flour * 0.75
price_for_1L_milk = price_of_kg_flour * 1.25
milk_needed_for_one_bread = price_for_1L_milk / 4

total_for_one_bread = price_of_kg_flour + price_of_eggs \
                      + milk_needed_for_one_bread

while budget > total_for_one_bread:
    current_check += total_for_one_bread
    budget -= total_for_one_bread
    bred_count += 1
    eggs_count += 3

    if bred_count % 3 == 0:
        eggs_count -= (bred_count - 2)

money_left = budget

print(f'You made {bred_count} loaves of Easter bread! \
Now you have {eggs_count} eggs and {money_left:.2f}BGN left.')
