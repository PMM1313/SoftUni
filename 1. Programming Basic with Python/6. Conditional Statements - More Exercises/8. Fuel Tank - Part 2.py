
fuel_type = str(input())
fuel = float(input())
club_card = str(input())

gasoline_price_per_l = 2.22
diesel_price_per_l = 2.33
gas_price_per_l = 0.93

club_card_discount = 0
fuel_price_per_l = 0

if club_card == 'Yes':
    if fuel_type == 'Gas':
        club_card_discount = 0.08
    elif fuel_type == 'Diesel':
        club_card_discount = 0.12
    elif fuel_type == 'Gasoline':
        club_card_discount = 0.18

if fuel_type == 'Gas':
    fuel_price_per_l = gas_price_per_l
elif fuel_type == 'Diesel':
    fuel_price_per_l = diesel_price_per_l
elif fuel_type == 'Gasoline':
    fuel_price_per_l = gasoline_price_per_l

if 0 <= fuel <= 19:
    fuel_liters_discount = 0
elif 20 <= fuel <= 25:
    fuel_liters_discount = 0.08
else:
    fuel_liters_discount = 0.10

club_card_fuel_cost_per_l = fuel_price_per_l - club_card_discount
total_cost_for_fuel = fuel * club_card_fuel_cost_per_l
discount_for_quantity = total_cost_for_fuel * fuel_liters_discount
total_cost_for_fuel = total_cost_for_fuel - discount_for_quantity
print(f'{total_cost_for_fuel:.2f} lv.')
