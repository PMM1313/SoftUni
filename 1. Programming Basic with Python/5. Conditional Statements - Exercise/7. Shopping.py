
budget = float(input())
number_of_videocards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

# prices:
price_of_videocards = 250.00
price_of_processors = (price_of_videocards * number_of_videocards * 0.35)
price_of_ram = (price_of_videocards * number_of_videocards * 0.10)

# total sum
sum_for_videocards = number_of_videocards * price_of_videocards
sum_for_processors = number_of_processors * price_of_processors
sum_for_ram = number_of_ram * price_of_ram
sum_of_all = sum_for_videocards + sum_for_processors + sum_for_ram

if number_of_videocards > number_of_processors:
    discount = sum_of_all * 0.15
    sum_of_all = sum_of_all - discount

if budget >= sum_of_all:
    money_left = budget - sum_of_all
    print(f'You have {money_left:.2f} leva left!')
else:
    needed_money = sum_of_all - budget
    print(f'Not enough money! You need {needed_money:.2f} leva more!')
