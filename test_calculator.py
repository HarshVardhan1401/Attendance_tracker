import unittest
from src import calculator as c
from src.models import Subject


class TestCalculator(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(c.percentage(45, 60), 75.0)
        self.assertEqual(c.percentage(0, 0), 0.0)

    def test_overall(self):
        subs = [Subject("A", 10, 10), Subject("B", 10, 5)]
        self.assertEqual(c.overall_percentage(subs), 75.0)

    def test_classes_needed(self):
        self.assertEqual(c.classes_needed(6, 10), 6)   # 12/16 = 75%
        self.assertEqual(c.classes_needed(9, 10), 0)

    def test_classes_can_skip(self):
        self.assertEqual(c.classes_can_skip(9, 10), 2)  # 9/12 = 75%
        self.assertEqual(c.classes_can_skip(5, 10), 0)

    def test_status(self):
        self.assertEqual(c.status(80), "SAFE")
        self.assertEqual(c.status(60), "LOW")


if __name__ == "__main__":
    unittest.main()
