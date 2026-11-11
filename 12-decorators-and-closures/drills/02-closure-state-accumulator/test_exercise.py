"""
Unit tests for Drill 02: Closure State Accumulator
"""
import unittest
from exercise import make_accumulator


class TestClosureState(unittest.TestCase):

    def test_independent_accumulators(self):
        acc1 = make_accumulator(0)
        acc2 = make_accumulator(100)

        self.assertEqual(acc1(5), 5)
        self.assertEqual(acc1(10), 15)

        self.assertEqual(acc2(50), 150)
        self.assertEqual(acc1(1), 16) # Verify acc1 was unaffected by acc2


if __name__ == "__main__":
    unittest.main()
