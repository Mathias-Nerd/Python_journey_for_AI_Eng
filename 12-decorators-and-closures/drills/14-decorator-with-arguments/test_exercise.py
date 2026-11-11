"""
Unit tests for Drill 14: Decorator with Arguments
"""
import unittest
from exercise import repeat


class TestRepeatDecorator(unittest.TestCase):

    def test_repeat_execution(self):
        count = 0

        @repeat(num_times=4)
        def increment():
            nonlocal count
            count += 1
            return count

        ans = increment()
        self.assertEqual(ans, 4)
        self.assertEqual(count, 4)


if __name__ == "__main__":
    unittest.main()
