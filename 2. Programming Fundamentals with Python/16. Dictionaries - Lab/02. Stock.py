# Read the input for stock items
stock_input = input().strip()
stock_items = stock_input.split()

# Create an empty dictionary to store stock
stock = {}
for i in range(0, len(stock_items), 2):
    key = stock_items[i]
    value = int(stock_items[i + 1])
    stock[key] = value

# Read the input for products to search for
search_input = input().strip()
search_products = search_input.split()

# Check each product in search_products
for product in search_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")