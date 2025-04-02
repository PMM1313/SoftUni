from project.senior_student import SeniorStudent
from unittest import TestCase, main


class TestSeniorStudent(TestCase):

    student_it = "0123"
    name = "Test Student"
    student_gpa = 4.5

    def setUp(self):
        self.student = SeniorStudent(self.student_it, self.name, self.student_gpa)

    def test_init(self):
        self.assertEqual(self.student_it, self.student.student_id)
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.student_gpa, self.student.student_gpa)
        self.assertEqual(0, len(self.student.colleges))

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as e:
            self.student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.student_id = " 123 "
        self.assertEqual("Student ID must be at least 4 digits long!", str(e.exception))

    def test_student_id_valid(self):
        self.student.student_id = " 12345 "
        self.assertEqual("12345", self.student.student_id)

    def test_name_valid(self):
        self.student.name = "John Doe"
        self.assertEqual("John Does", self.student.name)

        self.student.name = "  John Doe "
        self.assertEqual("John Does", self.student.name)

    def test_name_empty(self):
        with self.assertRaises(ValueError) as e:
            self.student.name = ""
            self.assertEqual("Student name cannot be null or empty!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.name = "  "
            self.assertEqual("Student name cannot be null or empty!", str(e.exception))

    def test_student_gpa_valid(self):
        self.student.student_gpa = 1.002
        self.assertEqual(1.002, self.student.student_gpa)

    def test_student_gpa_raises(self):
        with self.assertRaises(ValueError) as e:
            self.student.student_gpa = 0.99
            self.assertEqual("Student GPA must be more than 1.0!", str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.student_gpa = 1
            self.assertEqual("Student GPA must be more than 1.0!", str(e.exception))

    def test_apply_to_college_low_gpa(self):
        actual = self.student.apply_to_college(4.6, "Harvard")
        expected = f"Application failed"
        self.assertEqual(expected, actual)
        self.assertEqual(0, len(self.student.colleges))

    def test_apply_to_college_success(self):
        actual = self.student.apply_to_college(4.2, "Harvard")
        expected = f"{self.name} successfully applied to Harvard."
        self.assertEqual(expected, actual)
        self.assertEqual(1, len(self.student.colleges))

    def test_apply_to_college_multi(self):
        self.student.apply_to_college(4.2, "Harvard")
        self.student.apply_to_college(4.2, "MIT")
        self.student.apply_to_college(4.2, "Harvard")
        self.student.apply_to_college(4.2, "MIT")
        self.assertEqual(2, len(self.student.colleges))

    def test_update_gpa_invalid(self):
        actual = self.student.update_gpa(0.9)
        expected = "The GPA has not been changed!"
        self.assertEqual(expected, actual)
        self.assertEqual(4.5, self.student.student_gpa)

        actual = self.student.update_gpa(1)
        expected = "The GPA has not been changed!"
        self.assertEqual(expected, actual)
        self.assertEqual(4.5, self.student.student_gpa)

    def test_update_gpa_success(self):
        actual = self.student.update_gpa(1.1)
        expected = "Student GPA was successfully updated."
        self.assertEqual(expected, actual)
        self.assertEqual(1.1, self.student.student_gpa)

    def test__eq__equal(self):
        student2 = SeniorStudent("65656", "Jane Doe", 4.5)
        self.assertTrue(self.student == student2)

    def test__eq__not_equal(self):
        student2 = SeniorStudent("65656", "Jane Doe", 4)
        self.assertFalse(self.student == student2)


if __name__ == "__main__":
    main()