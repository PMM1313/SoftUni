coin_values = [200, 100, 50, 20, 10, 5, 2, 1]
amount = float(input())

amount_cents = int(round(amount * 100))
coins_count = 0

for coin in coin_values:
    if amount_cents >= coin:
        coins_count += amount_cents // coin
        amount_cents %= coin

print(coins_count)
