def calculate_result(operator, num1, num2):
    if operator == 'multiply':
        return num1 * num2
    elif operator == 'divide':
        return int(num1 / num2)
    elif operator == 'add':
        return num1 + num2
    elif operator == 'subtract':
        return num1 - num2


operator = input()
first_number = int(input())
second_number = int(input())
result = calculate_result(operator, first_number, second_number)
print(result)
