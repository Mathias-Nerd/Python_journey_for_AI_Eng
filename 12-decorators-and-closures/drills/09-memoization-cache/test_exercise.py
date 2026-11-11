"""
Unit tests for Drill 09: Memoization Cache
"""
import unittest
from exercise import memoize


class TestMemoizeDecorator(unittest.TestCase):

    def test_cache_hits(self):
        runs = 0

        @memoize
        def compute(x):
            nonlocal runs
            runs += 1
            return x + 10

        self.assertEqual(compute(5), 15)
        self.assertEqual(runs, 1)

        self.assertEqual(compute(5), 15)
        self.assertEqual(runs, 1) # Cache hit!

        self.assertEqual(compute(6), 16)
        self.assertEqual(runs, 2)


if __name__ == "__main__":
    unittest.main()
