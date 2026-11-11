"""
Unit tests for Drill 07: Call Counter
"""
import unittest
from exercise import count_calls


class TestCallCounter(unittest.TestCase):

    def test_call_counts(self):
        @count_calls
        def add(a, b): return a + b

        self.assertEqual(add.calls, 0)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add.calls, 1)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add.calls, 2)


if __name__ == "__main__":
    unittest.main()
