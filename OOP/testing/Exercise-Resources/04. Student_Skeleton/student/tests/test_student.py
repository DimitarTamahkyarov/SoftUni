import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Ivan")
        self.other_student = Student("Gosho", {"C#": ["note1", "note2", "note3"], "Python": ["note1", "note2"]})

    def test__init__with_name_only(self):
        self.assertEqual(self.student.name, "Ivan")
        self.assertEqual(self.student.courses, {})

    def test__init__with_name_and_courses(self):
        self.assertEqual(self.other_student.name, "Gosho")
        self.assertEqual(self.other_student.courses, {"C#": ["note1", "note2", "note3"], "Python": ["note1", "note2"]})



if __name__ == "__main__":
    unittest.main()