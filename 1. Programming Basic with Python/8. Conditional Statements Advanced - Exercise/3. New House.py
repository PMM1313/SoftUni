type_of_flower = (input())
number_of_flowers = int(input())
budget = float(input())

price_of_flower = 0

# prices:
Roses = 5.00
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3.00
Gladiolus = 2.50

if number_of_flowers <= 0:
    exit()

if type_of_flower == "Roses":
    price_of_flower = Roses
    # discount - 10 % over 80
    if number_of_flowers > 80:
        price_of_flower *= 0.90
elif type_of_flower == "Dahlias":
    price_of_flower = Dahlias
    # discount - 15 % over 90
    if number_of_flowers > 90:
        price_of_flower *= 0.85
elif type_of_flower == "Tulips":
    price_of_flower = Tulips
    if number_of_flowers > 80:
        price_of_flower *= 0.85
elif type_of_flower == "Narcissus":
    price_of_flower = Narcissus
    if number_of_flowers < 120:
        price_of_flower *= 1.15
elif type_of_flower == "Gladiolus":
    price_of_flower = Gladiolus
    if number_of_flowers < 80:
        price_of_flower *= 1.20
else:
    print(f'Invalid flower name')
    exit()

total_sum = number_of_flowers * price_of_flower

if total_sum <= budget:
    money_left = budget - total_sum
    print(f'Hey, you have a great garden with {number_of_flowers} {type_of_flower} and {money_left:.2f} leva left.')
else:
    money_needed = total_sum - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')
