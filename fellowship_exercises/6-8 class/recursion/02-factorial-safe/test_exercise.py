"""
Unit tests for Drill 02: Safe Factorial
"""
import ast
import inspect
import unittest
from exercise import factorial


class TestFactorialSafe(unittest.TestCase):

    def test_standard_cases(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)

    def test_base_case_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_invalid_types_raise_type_error(self):
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("4")
        with self.assertRaises(TypeError):
            factorial(True)
        with self.assertRaises(TypeError):
            factorial(False)
        with self.assertRaises(TypeError):
            factorial(None)

    def test_no_forbidden_constructs(self):
        source = inspect.getsource(factorial)
        parsed = ast.parse(source)

        for node in ast.walk(parsed):
            self.assertNotIsInstance(
                node, (ast.For, ast.While),
                "Loops are not allowed. Use recursion."
            )
            if isinstance(node, ast.Attribute) and node.attr == "factorial":
                self.fail("math.factorial is not allowed.")


if __name__ == "__main__":
    unittest.main()
