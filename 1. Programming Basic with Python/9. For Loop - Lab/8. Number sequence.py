
n = int(input())

# Инициализация на променливите за най-голямото и най-малкото число
max_number = float('-inf')  # Начална стойност за най-голямото число
min_number = float('inf')   # Начална стойност за най-малкото число

# Четене на числата и намиране на най-голямото и най-малкото число
for _ in range(n):
    current_number = int(input())

    # Проверка за най-голямото число
    if current_number > max_number:
        max_number = current_number

    # Проверка за най-малкото число
    if current_number < min_number:
        min_number = current_number

# Отпечатване на резултатите
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
