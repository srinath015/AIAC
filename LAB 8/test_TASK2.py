import unittest
from TASK2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_valid_grades(self):
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(89.9), "B")
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(79.9), "C")
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(69.9), "D")
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(59.9), "F")
        self.assertEqual(assign_grade(0), "F")

    def test_invalid_type(self):
        self.assertEqual(assign_grade("abc"), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade(None), "Invalid input: score must be a number.")
        self.assertEqual(assign_grade([90]), "Invalid input: score must be a number.")

    def test_out_of_range(self):
        self.assertEqual(assign_grade(-1), "Invalid input: score must be between 0 and 100.")
        self.assertEqual(assign_grade(101), "Invalid input: score must be between 0 and 100.")

if __name__ == "__main__":
    unittest.main()