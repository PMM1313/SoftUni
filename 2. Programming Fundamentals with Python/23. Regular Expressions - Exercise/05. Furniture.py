import re

bouth_furniture = []
total_cost = 0
command = input()
pattern = ">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"


while command != "Purchase":
    match = re.search(pattern, command)

    if match:

        furniture, price, quantity = match.groups()
        bouth_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

    command = input()

print(f'Bought furniture:')

for furniture in bouth_furniture:
    print(furniture)

print(f'Total money spend: {total_cost:.2f}')