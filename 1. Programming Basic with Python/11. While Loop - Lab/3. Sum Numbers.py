
number = int(input())


total_numbers = 0

while total_numbers < number:
    numbers = int(input())
    total_numbers += numbers
    if number <= int(total_numbers):
        break
print(f'{total_numbers}')
