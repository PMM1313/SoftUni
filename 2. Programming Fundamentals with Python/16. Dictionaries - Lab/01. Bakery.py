# Read the input line
input_line = input().strip()

# Split the input line into a list of strings
items = input_line.split()

# Create an empty dictionary to store the results
stock = {}

# Iterate through the list in steps of 2
for i in range(0, len(items), 2):
    # Extract the key (food item) and value (quantity)
    key = items[i]
    value = int(items[i + 1])  # Convert value to integer

    # Add key-value pair to the dictionary
    stock[key] = value

# Print the resulting dictionary
print(stock)