"""
Unit tests for Drill 10: Input Type Enforcer
"""
import unittest
from exercise import enforce_types


class TestTypeEnforcer(unittest.TestCase):

    def test_valid_types(self):
        @enforce_types(int, int)
        def add(a, b): return a + b
        self.assertEqual(add(2, 3), 5)

    def test_invalid_types_raise(self):
        @enforce_types(int, str)
        def process(count, tag): return f"{tag}_{count}"

        with self.assertRaises(TypeError):
            process("5", "tag")

        with self.assertRaises(TypeError):
            process(True, "tag") # Guard bool subclasses int


if __name__ == "__main__":
    unittest.main()
