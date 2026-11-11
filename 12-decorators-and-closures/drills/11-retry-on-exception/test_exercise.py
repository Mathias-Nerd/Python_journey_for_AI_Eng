"""
Unit tests for Drill 11: Retry on Exception
"""
import unittest
from exercise import retry


class TestRetry(unittest.TestCase):

    def test_eventual_success(self):
        count = 0

        @retry(max_attempts=3, exceptions=(ValueError,))
        def flaky():
            nonlocal count
            count += 1
            if count < 2:
                raise ValueError("Fail once")
            return "OK"

        self.assertEqual(flaky(), "OK")
        self.assertEqual(count, 2)

    def test_total_failure_raises(self):
        @retry(max_attempts=2, exceptions=(KeyError,))
        def broken():
            raise KeyError("Never succeeds")

        with self.assertRaises(KeyError):
            broken()


if __name__ == "__main__":
    unittest.main()
