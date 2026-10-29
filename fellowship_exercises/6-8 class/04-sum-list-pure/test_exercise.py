"""
Unit tests for Drill 04: Pure Recursive List Sum
"""
import ast
import inspect
import unittest
from exercise import sum_list


class TestSumListPure(unittest.TestCase):

    def test_standard_integers(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([10, -5, 2]), 7)
        self.assertEqual(sum_list([42]), 42)

    def test_empty_list(self):
        self.assertEqual(sum_list([]), 0)

    def test_floats(self):
        self.assertAlmostEqual(sum_list([1.5, 2.5, 3.0]), 7.0)

    def test_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            sum_list("123")
        with self.assertRaises(TypeError):
            sum_list(123)
        with self.assertRaises(TypeError):
            sum_list(None)

    def test_no_forbidden_constructs(self):
        source = inspect.getsource(sum_list)
        parsed = ast.parse(source)

        for node in ast.walk(parsed):
            self.assertNotIsInstance(
                node, (ast.For, ast.While),
                "Loops are not allowed."
            )
            self.assertNotIsInstance(
                node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
                "Comprehensions are not allowed."
            )
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ["sum"], "Built-in sum() is forbidden.")
            # Verify no slicing like numbers[1:]
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                self.fail("List slicing creates O(n) memory copies per call. Use the index pointer.")


if __name__ == "__main__":
    unittest.main()
