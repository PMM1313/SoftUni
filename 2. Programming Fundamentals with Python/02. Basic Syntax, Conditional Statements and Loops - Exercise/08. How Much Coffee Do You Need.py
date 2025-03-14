
number_of_coffees = 0

while True:
    command = input()

    if command == 'END':
        break
    elif command == 'coding' or command == 'cat' or command == 'cat' or command == 'movie':
        number_of_coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        number_of_coffees += 2

if number_of_coffees > 5:
    print('You need extra sleep')
else:
    print(number_of_coffees)

