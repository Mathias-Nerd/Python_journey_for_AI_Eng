"""
Unit tests for Drill 01: Functions as First-Class Citizens
"""
import unittest
from exercise import make_multiplier, apply_pipeline


class TestFirstClassFunctions(unittest.TestCase):

    def test_make_multiplier(self):
        triple = make_multiplier(3)
        self.assertEqual(triple(4), 12)
        self.assertEqual(triple(0), 0)

    def test_apply_pipeline(self):
        double = make_multiplier(2)
        add_five = lambda x: x + 5
        res = apply_pipeline([1, 2, 3], [double, add_five])
        self.assertEqual(res, [7, 9, 11])


if __name__ == "__main__":
    unittest.main()
