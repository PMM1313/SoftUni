
budget = float(input())
number_of_extras = int(input())
price_of_clothing = float(input())

decor = budget*0.10

if number_of_extras > 150:
    cloth_discount = price_of_clothing*0.10
    price_of_clothing = price_of_clothing - cloth_discount

if decor + price_of_clothing * number_of_extras > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {decor + price_of_clothing * number_of_extras - budget:.2f} leva more.')

if decor + price_of_clothing * number_of_extras <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {budget - decor - price_of_clothing * number_of_extras:.2f} leva left.')

