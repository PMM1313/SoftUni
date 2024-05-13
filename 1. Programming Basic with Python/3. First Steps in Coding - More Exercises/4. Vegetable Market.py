
price_of_veg = float(input())
price_of_fruit = float(input())
kilos_of_veg = float(input())
kilos_of_fruit = float(input())

# lev to euro
euro = 1.94

# calculating profit in euro
all_profit = ((price_of_veg*kilos_of_veg) + (price_of_fruit*kilos_of_fruit)) / euro

print(F'{all_profit:.2f}')
