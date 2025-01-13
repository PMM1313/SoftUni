from collections import deque

# Input chocolates and milk
chocolates = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))

# Initialize milkshake count
milkshakes = 0

# Process while we can make milkshakes
while milkshakes < 5 and chocolates and milk:
    # Remove invalid chocolates and milk
    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    while milk and milk[0] <= 0:
        milk.popleft()

    # If any sequence becomes empty, break
    if not chocolates or not milk:
        break

    # Get the current chocolate and milk
    current_chocolate = chocolates[-1]
    current_milk = milk[0]

    if current_chocolate == current_milk:
        # Match found, make a milkshake
        milkshakes += 1
        chocolates.pop()  # Remove last chocolate
        milk.popleft()  # Remove first milk
    else:
        # No match, modify chocolate and rotate milk
        chocolates[-1] -= 5
        milk.append(milk.popleft())  # Move milk to the back

# Output results
if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

# Print remaining chocolates
if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

# Print remaining milk
if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")
