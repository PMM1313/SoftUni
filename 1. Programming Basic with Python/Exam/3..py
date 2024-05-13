
people_count = int(input())
season = input()

price_per_person = 0.0

if people_count <= 5:
    if season == "spring":
        price_per_person = 50.00
    elif season == "summer":
        price_per_person = 48.50
    elif season == "autumn":
        price_per_person = 60.00
    elif season == "winter":
        price_per_person = 86.00
else:
    if season == "spring":
        price_per_person = 48.00
    elif season == "summer":
        price_per_person = 45.00
    elif season == "autumn":
        price_per_person = 49.50
    elif season == "winter":
        price_per_person = 85.00

# discount
discount_or_extra = 0.0

if season == "summer":
    discount_or_extra = -0.15
elif season == "winter":
    discount_or_extra = 0.08

# total sum
total_price = people_count * price_per_person * (1 + discount_or_extra)

print(f"{total_price:.2f} leva.")
