
age = float(input())
sex = str(input())

address = 0

if sex == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')

elif sex == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
