"""
Unit tests for Drill 07: Fibonacci with Memoization
"""
import ast
import inspect
import unittest
from exercise import fibonacci


class TestFibonacciMemo(unittest.TestCase):

    def test_standard_values(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(10), 55)

    def test_large_n_requires_memoization(self):
        # Naive O(2^n) would freeze or take years for n=50.
        # Memoized O(n) takes less than 1 millisecond.
        self.assertEqual(fibonacci(50), 12586269025)

    def test_negative_raises_value_error(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            fibonacci(3.14)
        with self.assertRaises(TypeError):
            fibonacci("7")
        with self.assertRaises(TypeError):
            fibonacci(True)

    def test_no_loops(self):
        source = inspect.getsource(fibonacci)
        parsed = ast.parse(source)
        for node in ast.walk(parsed):
            self.assertNotIsInstance(node, (ast.For, ast.While), "Loops are not allowed.")


if __name__ == "__main__":
    unittest.main()
