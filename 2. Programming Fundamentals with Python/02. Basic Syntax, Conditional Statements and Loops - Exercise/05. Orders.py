number_of_orders = int(input())

total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_need_per_day = int(input())

    if 0.01 <= price_per_capsule <= 101.00 and days in range(1, 32) and capsules_need_per_day in range(1, 2001):
        total = price_per_capsule*capsules_need_per_day*days
        total_price += total
        print(f'The price for the coffee is: ${total:.2f}')

print(f'Total: ${total_price:.2f}')
