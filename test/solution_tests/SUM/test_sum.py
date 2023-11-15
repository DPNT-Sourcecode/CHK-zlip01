from unittest import TestCase
from solutions.SUM.sum_solution import compute

class TestSum(TestCase):
    def test_sum_one(self):
        self.assertEqual(compute(10, 10), 20)
    def test_sum_two(self):
        self.assertEqual(compute(0, 0), 0)
    def test_sum_three(self):
        self.assertEqual(compute(100, 100), 200)



