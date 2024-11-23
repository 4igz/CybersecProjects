import unittest
from password_strength_checker import check_password_strength

class TestPasswordStrengthChecker(unittest.TestCase):
    def test_short_password(self):
        # This is weak because it only meets 1 criteria, even though it's >8 characters long
        self.assertEqual(check_password_strength("abcaafsaa"), "Weak")

    def test_strong_password(self):
        # This is strong because it meets all 4 criteria and is atleast 8 characters long
        self.assertEqual(check_password_strength("Abcdefg1!"), "Strong")

    def test_empty_password(self):
        # This is weak because it's empty
        self.assertEqual(check_password_strength(""), "Weak")

    def test_weak_but_meets_all_criteria(self):
        # This is weak because it's only 7 characters long even though it meets all criteria
        self.assertEqual(check_password_strength("Abcef1!"), "Weak")


if __name__ == "__main__":
    unittest.main()