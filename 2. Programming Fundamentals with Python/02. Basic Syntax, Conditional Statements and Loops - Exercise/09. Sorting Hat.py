
while True:
    names = input()

    if names == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    elif names == 'Voldemort':
        print('You must not speak of that name!')
        break
    if len(names) < 5:
        print(f'{names} goes to Gryffindor.')
    elif len(names) == 5:
        print(f'{names} goes to Slytherin.')
    elif len(names) == 6:
        print(f'{names} goes to Ravenclaw.')
    elif len(names) > 6:
        print(f'{names} goes to Hufflepuff.')
