
product = str(input())
city = str(input())
quantity = float(input())

product_price = 0

if city == 'Sofia':
    # prices in sofia
    coffee_price = 0.50
    water_price = 0.80
    beer_price = 1.20
    sweets_price = 1.45
    peanuts_price = 1.60
elif city == 'Plovdiv':
    coffee_price = 0.40
    water_price = 0.70
    beer_price = 1.15
    sweets_price = 1.30
    peanuts_price = 1.50
else:
    coffee_price = 0.45
    water_price = 0.70
    beer_price = 1.10
    sweets_price = 1.35
    peanuts_price = 1.55

if product == 'coffee':
    product_price = coffee_price
elif product == 'water':
    product_price = water_price
elif product == 'beer':
    product_price = beer_price
elif product == 'sweets':
    product_price = sweets_price
elif product == 'peanuts':
    product_price = peanuts_price


# calculating prices:
total = product_price * quantity
print(total)
