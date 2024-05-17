string_number = int(input())

string = ''

for n in range(string_number):
    string = input()

    if ',' not in string and '.' not in string and '_' not in string:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
