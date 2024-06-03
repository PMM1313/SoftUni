items_with_prices = list(input().split("|"))
budget = float(input())

items_both = []
items_new_price = []
profit = 0


for item in items_with_prices:
    item = item.split('->')
    item_type = item[0]
    item_price = float(item[1])

    if item_type == 'Clothes' and item_price <= 50.00 and item_price <= budget:
        budget -= item_price
        items_both.append(item_price)

    elif item_type == 'Shoes' and item_price <= 35.00 and item_price <= budget:
        budget -= item_price
        items_both.append(item_price)

    elif item_type == 'Accessories' and item_price <= 20.50 and item_price <= budget:
        budget -= item_price
        items_both.append(item_price)

for both_item in items_both:
    increased_price = both_item * 1.4
    items_new_price.append(increased_price)
    budget += increased_price
    profit += (increased_price - both_item)

print(" ".join(f'{price:.2f}' for price in items_new_price))
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
