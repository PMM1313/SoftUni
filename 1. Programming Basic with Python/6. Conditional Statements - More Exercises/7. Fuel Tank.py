
fuel_type = str(input())
fuel_in_reservoir = float(input())

fuel_needed = 25

if fuel_type == 'Diesel' or fuel_type == 'Gasoline' or fuel_type == 'Gas':
    if fuel_in_reservoir >= fuel_needed:
        print(f'You have enough {fuel_type.lower()}.')
    else:
        print(f'Fill your tank with {fuel_type.lower()}!')
else:
    print(f'Invalid fuel!')
