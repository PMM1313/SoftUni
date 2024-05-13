
fish1_price = float(input())
fish2_price = float(input())
fish3_kilos = float(input())
fish4_kilos = float(input())
mussels_kilos = int(input())

# prices
mussels_price = 7.50
fish3_price = fish1_price + (0.6 * fish1_price)
fish3_total = fish3_price * fish3_kilos
fish4_price = fish2_price + (0.8 * fish2_price)
fish4_total = fish4_price * fish4_kilos
mussels_total = mussels_kilos * mussels_price

# calculating all the stuff:
total_cost = (fish3_total + fish4_total + mussels_total)

total_cost_rounded = round(total_cost, 2)
print(f"{total_cost_rounded:.2f}")
