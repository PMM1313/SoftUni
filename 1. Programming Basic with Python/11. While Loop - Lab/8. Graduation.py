
name = str(input())
grade = 0.00
sum_grades = 0.00
excluded = 0
klass = 0

while klass < 12 and excluded < 2:
    grade = float(input())

    if grade < 4.00:
        excluded += 1
    elif grade >= 4.00:
        sum_grades += grade
        klass += 1

if excluded >= 2:
    print(f'{name} has been excluded at {klass + 1} grade')

if klass == 12:
    average = sum_grades / klass
    print(f'{name} graduated. Average grade: {average:.2f}')

