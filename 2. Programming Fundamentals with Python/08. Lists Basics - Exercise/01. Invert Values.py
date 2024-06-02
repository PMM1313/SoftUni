string = input()

numbers = []


for number in string.split(' '):
    number = int(number)
    opposite_number = number * -1
    numbers.append(opposite_number)

print(numbers)
