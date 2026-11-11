"""
Unit tests for Drill 15: Optional Arguments Decorator
"""
import unittest
from exercise import prefix


class TestOptionalArgs(unittest.TestCase):

    def test_without_parentheses(self):
        @prefix
        def get_status(): return "ready"
        self.assertEqual(get_status(), "[INFO] ready")

    def test_with_arguments(self):
        @prefix(tag="ALERT")
        def get_warn(): return "failure"
        self.assertEqual(get_warn(), "[ALERT] failure")


if __name__ == "__main__":
    unittest.main()
