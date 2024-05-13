
number = input()

biggest_number = -10000000000000

while number != 'Stop':
    num = int(number)

    if num > biggest_number:
        biggest_number = num

    number = input()

print(biggest_number)

