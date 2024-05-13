
budget = float(input())
season = str(input())

money_spend = 0
destination = ''
hotel_or_camping = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        hotel_or_camping = 'Camp'
        money_spend = budget * 0.30
    elif season == 'winter':
        hotel_or_camping = 'Hotel'
        money_spend = budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        hotel_or_camping = 'Camp'
        money_spend = budget * 0.40
    elif season == 'winter':
        hotel_or_camping = 'Hotel'
        money_spend = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    hotel_or_camping = 'Hotel'
    money_spend = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{hotel_or_camping} - {money_spend:.2f}')
