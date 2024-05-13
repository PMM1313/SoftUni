upper_limit_1 = int(input())
upper_limit_2 = int(input())
upper_limit_3 = int(input())

for i in range(2, upper_limit_1 + 1, 2):
    for j in [2, 3, 5, 7]:  # Прости числа в интервала [2...7]
        if j <= upper_limit_2:  # Проверка дали простото число е в границите на горния лимит
            for k in range(2, upper_limit_3 + 1, 2):
                print(f"{i}{j}{k}")
