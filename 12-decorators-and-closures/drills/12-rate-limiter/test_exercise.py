"""
Unit tests for Drill 12: Rate Limiter
"""
import unittest
from exercise import rate_limit


class TestRateLimiter(unittest.TestCase):

    def test_rate_limiting(self):
        @rate_limit(max_calls=2, period_seconds=1.0)
        def request(): return True

        self.assertTrue(request())
        self.assertTrue(request())
        with self.assertRaises(RuntimeError):
            request()


if __name__ == "__main__":
    unittest.main()
