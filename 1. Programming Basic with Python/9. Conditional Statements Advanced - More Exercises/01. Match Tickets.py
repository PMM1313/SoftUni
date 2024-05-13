budget = float(input())
ticket_type = str(input())
number_of_people = int(input())

if ticket_type == 'VIP':
    ticket_price = 499.99
elif ticket_type == 'Normal':
    ticket_price = 249.99

# calculating money left for tickets
if 1 <= number_of_people <= 4:
    money_left = budget * 0.25
elif 5 <= number_of_people <= 9:
    money_left = budget * 0.40
elif 10 <= number_of_people <= 24:
    money_left = budget * 0.50
elif 25 <= number_of_people <= 49:
    money_left = budget * 0.60
elif 50 <= number_of_people:
    money_left = budget * 0.75

ticket_total_price = ticket_price * number_of_people

if money_left > ticket_total_price:
    left = money_left - ticket_total_price
    print(f"Yes! You have {left:.2f} leva left.")
else:
    more_needed = ticket_total_price - money_left
    print(f'Not enough money! You need {more_needed:.2f} leva.')
