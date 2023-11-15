from solutions.SUM import compute
import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(compute(5, 5) == 10)

