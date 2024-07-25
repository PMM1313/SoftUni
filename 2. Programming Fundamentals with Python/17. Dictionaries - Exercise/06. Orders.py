products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        products[name]['quantity'] += quantity
        products[name]['price'] = price
    else:
        products[name] = {'price': price, 'quantity': quantity}

for name, details in products.items():
    total_price = details['price'] * details['quantity']
    print(f"{name} -> {total_price:.2f}")