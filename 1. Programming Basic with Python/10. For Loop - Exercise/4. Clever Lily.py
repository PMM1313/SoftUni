age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
toys = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        total_money += 10 + (i // 2 - 1) * 10  # на всяко четно раждане Лили получава 10 лева и сумата се увеличава с 10 лева за всяко следващо четно раждане
        total_money -= 1  # брат ѝ взима по 1 лев
    else:
        toys += 1

total_money += toys * toy_price  # Лили продава играчките
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
