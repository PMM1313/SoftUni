# Initialize an empty dictionary to store products and quantities
stock = {}

# Read input until "statistics" command is encountered
while True:
    line = input().strip()
    if line == "statistics":
        break

    # Split the input line into product and quantity
    product, quantity = line.split(": ")
    quantity = int(quantity)

    # Check if product already exists in stock
    if product in stock:
        stock[product] += quantity
    else:
        stock[product] = quantity

# Output the statistics
print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

total_products = len(stock)  # Total unique products
total_quantity = sum(stock.values())  # Sum of all quantities

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
