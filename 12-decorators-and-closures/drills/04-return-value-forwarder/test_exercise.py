"""
Unit tests for Drill 04: Return Value Forwarder
"""
import unittest
from exercise import forward_result


class TestReturnValueForwarder(unittest.TestCase):

    def test_returns_int(self):
        @forward_result
        def compute(x): return x * 10
        self.assertEqual(compute(5), 50)

    def test_returns_falsy_values(self):
        @forward_result
        def get_empty(): return []
        self.assertEqual(get_empty(), [])

        @forward_result
        def get_none(): return None
        self.assertIsNone(get_none())


if __name__ == "__main__":
    unittest.main()
