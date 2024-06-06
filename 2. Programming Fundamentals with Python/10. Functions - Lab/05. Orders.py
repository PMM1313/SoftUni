def calculate_order(product, quantity):
    total_sum = 0
    if product == 'coffee':
        price = 1.50
        total_sum += price * quantity
    elif product == 'water':
        price = 1.00
        total_sum += price * quantity
    elif product == 'coke':
        price = 1.40
        total_sum += price * quantity
    elif product == 'snacks':
        price = 2.00
        total_sum += price * quantity
    return float(total_sum)


product = input()
quantity = int(input())
total_sum = calculate_order(product, quantity)
print(f'{total_sum:.2f}')
