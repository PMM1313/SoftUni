import math

wine_field_sq_m = int(input())
yield_per_sq_m = float(input())
needed_l_wine = int(input())
number_of_workers = int(input())

# total harvest
total_harvest = wine_field_sq_m * yield_per_sq_m
harvest_for_wine_production = total_harvest * 0.40

# wine production:
grape_to_wine_ratio = 2.5
wine_produced = harvest_for_wine_production / grape_to_wine_ratio

if wine_produced < needed_l_wine:
    needed_wine = needed_l_wine - wine_produced
    print(f'It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.')
if wine_produced >= needed_l_wine:
    surplus_wine = wine_produced - needed_l_wine
    liters_per_worker = surplus_wine / number_of_workers
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(surplus_wine)} liters left -> {math.ceil(liters_per_worker)} liters per person.')
