
fruit = input().lower()
day_of_week = input().lower()
quantity = float(input())

# price check
prices = {
    'banana': {'weekday': 2.50, 'weekend': 2.70},
    'apple': {'weekday': 1.20, 'weekend': 1.25},
    'orange': {'weekday': 0.85, 'weekend': 0.90},
    'grapefruit': {'weekday': 1.45, 'weekend': 1.60},
    'kiwi': {'weekday': 2.70, 'weekend': 3.00},
    'pineapple': {'weekday': 5.50, 'weekend': 5.60},
    'grapes': {'weekday': 3.85, 'weekend': 4.20}
}

# proverka za validnost
if fruit in prices and day_of_week in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
    price = prices[fruit][('weekday', 'weekend')['saturday' in day_of_week or 'sunday' in day_of_week]]
    total_price = price * quantity
    print(f'{total_price:.2f}')
else:
    print('error')
