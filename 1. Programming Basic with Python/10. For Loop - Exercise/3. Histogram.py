# Четем броя на числата number_of_models
n = int(input())

# Създаваме празен списък, в който ще съхраняваме числата
numbers = []

# Четем number_of_models числа и ги добавяме в списъка
for i in range(n):
    number = int(input())
    numbers.append(number)

# Инициализираме променливи за броя на числата в различните интервали
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

# Проходим през всяко число и увеличаваме броя в съответния интервал
for num in numbers:
    if num < 200:
        count_p1 += 1
    elif 200 <= num <= 399:
        count_p2 += 1
    elif 400 <= num <= 599:
        count_p3 += 1
    elif 600 <= num <= 799:
        count_p4 += 1
    else:
        count_p5 += 1

# Изчисляваме процентите
percentage_p1 = count_p1 / n * 100
percentage_p2 = count_p2 / n * 100
percentage_p3 = count_p3 / n * 100
percentage_p4 = count_p4 / n * 100
percentage_p5 = count_p5 / n * 100

# Отпечатваме резултата
print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")
