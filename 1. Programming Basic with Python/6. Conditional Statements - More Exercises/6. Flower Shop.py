import math

number_of_magnolias = int(input())
number_of_ziumbul = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
cost_of_gift = float(input())

# flower prices:
PRICE_OF_MAGNOLIAS = 3.25
PRICE_OF_ZIUMBUL = 4
PRICE_OF_ROSES = 3.50
PRICE_OF_CACTUSE = 8

# calculating all the stuff:

magnolias = number_of_magnolias * PRICE_OF_MAGNOLIAS
ziumbul = number_of_ziumbul * PRICE_OF_ZIUMBUL
roses = number_of_roses * PRICE_OF_ROSES
cactuses = number_of_cactuses * PRICE_OF_CACTUSE

total_sum = magnolias + ziumbul + roses + cactuses

# 5% taxes form total:
taxes = (total_sum * 0.05)
total_sum_minus_taxes = total_sum - taxes

if total_sum_minus_taxes >= cost_of_gift:
    money_left = total_sum_minus_taxes - cost_of_gift
    money_left_rounded = math.floor(money_left)
    print(f'She is left with {money_left_rounded} leva.')
else:
    money_needed = cost_of_gift - total_sum_minus_taxes
    money_needed_rounded = math.ceil(money_needed)
    print(f'She will have to borrow {money_needed_rounded} leva.')
