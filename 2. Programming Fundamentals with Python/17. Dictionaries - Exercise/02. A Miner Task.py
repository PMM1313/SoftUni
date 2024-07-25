mine = {}
resource = input()

while resource != "stop":
    quantity = int(input())

    # Update the quantity of the resource in the dictionary
    if resource in mine:
        mine[resource] += quantity
    else:
        mine[resource] = quantity

    # Get the next resource
    resource = input()

# Print the resources and their quantities
for resource, quantity in mine.items():
    print(f"{resource} -> {quantity}")