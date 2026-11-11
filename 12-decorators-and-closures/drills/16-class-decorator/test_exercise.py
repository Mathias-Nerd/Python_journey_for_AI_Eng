"""
Unit tests for Drill 16: Class Decorator
"""
import unittest
from exercise import add_repr


class TestClassDecorator(unittest.TestCase):

    def test_injected_repr(self):
        @add_repr
        class User:
            def __init__(self, uid, active):
                self.uid = uid
                self.active = active

        u = User(10, True)
        self.assertEqual(repr(u), "User(uid=10, active=True)")


if __name__ == "__main__":
    unittest.main()
