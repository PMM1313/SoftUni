number_of_student = int(input())

students = {}
for _ in range(number_of_student):
    name, grade_as_string = tuple(input().split())
    grade = float(grade_as_string)

    if name not in students:
        students[name] = []

    students[name].append(grade)

for name, grades in students.items():
    formated_grade = [str(f'{grade:.2f}') for grade in grades]
    avg_grade = sum(grades)/len(grades)
    print(f"{name} -> {' '.join(formated_grade)} (avg: {avg_grade:.2f})")