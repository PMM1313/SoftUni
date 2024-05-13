
tabs_count = int(input())
salary = int(input())

# Променлива за остатъка от заплатата
remaining_salary = salary

# Проверка за всяка отворена страница
for _ in range(tabs_count):
    website = input()

    if website == "Facebook":
        remaining_salary -= 150
    elif website == "Instagram":
        remaining_salary -= 100
    elif website == "Reddit":
        remaining_salary -= 50

    # Проверка за отрицателна заплата
    if remaining_salary <= 0:
        print("You have lost your salary.")
        break


if remaining_salary > 0:
    print(remaining_salary)
