"""
Unit tests for Drill 17: Singleton Decorator
"""
import unittest
from exercise import singleton


class TestSingleton(unittest.TestCase):

    def test_single_instance(self):
        @singleton
        class Config:
            def __init__(self):
                self.setting = "default"

        c1 = Config()
        c2 = Config()
        self.assertIs(c1, c2)
        c1.setting = "updated"
        self.assertEqual(c2.setting, "updated")


if __name__ == "__main__":
    unittest.main()
