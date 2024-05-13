
city = input().lower()
sales_volume = float(input())

# Проверка за валиден град и обем на продажби
if sales_volume < 0 or city not in ['sofia', 'varna', 'plovdiv']:
    print('error')
else:
    # Изчисляване на търговската комисионна според горната таблица
    commission_rates = {
        'sofia': [0.05, 0.07, 0.08, 0.12],
        'varna': [0.045, 0.075, 0.10, 0.13],
        'plovdiv': [0.055, 0.08, 0.12, 0.145]
    }

    if sales_volume <= 500:
        commission_rate = commission_rates[city][0]
    elif 500 < sales_volume <= 1000:
        commission_rate = commission_rates[city][1]
    elif 1000 < sales_volume <= 10000:
        commission_rate = commission_rates[city][2]
    else:
        commission_rate = commission_rates[city][3]

    # Изчисляване на търговската комисионна
    commission = sales_volume * commission_rate
    print(f'{commission:.2f}')
