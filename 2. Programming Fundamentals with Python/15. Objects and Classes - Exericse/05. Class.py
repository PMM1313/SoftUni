class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return round(sum(self.grades) / len(self.grades), 2)
        return 0

    def __repr__(self):
        average_grade = self.get_average_grade()
        students_str = ", ".join(self.students)
        return f"The students in {self.name}: {students_str}. Average grade: {average_grade}"

# Test code
a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)