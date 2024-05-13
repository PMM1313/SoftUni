destinations = {}

while True:
    destination = input()
    if destination == "End":
        break

    minimum_budget = float(input())
    destinations[destination] = minimum_budget

    savings = 0
    while savings < minimum_budget:
        amount_saved = float(input())
        savings += amount_saved

    print(f"Going to {destination}!")
