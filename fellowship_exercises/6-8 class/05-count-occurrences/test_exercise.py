"""
Unit tests for Drill 05: Count Target Occurrences
"""
import ast
import inspect
import unittest
from exercise import count_occurrences


class TestCountOccurrences(unittest.TestCase):

    def test_standard_counts(self):
        self.assertEqual(count_occurrences([1, 2, 3, 2, 4, 2], 2), 3)
        self.assertEqual(count_occurrences(["a", "b", "a", "c"], "a"), 2)
        self.assertEqual(count_occurrences([True, False, True], True), 2)

    def test_target_not_present(self):
        self.assertEqual(count_occurrences([1, 2, 3], 99), 0)
        self.assertEqual(count_occurrences([], 5), 0)

    def test_type_error_on_non_list(self):
        with self.assertRaises(TypeError):
            count_occurrences("abc", "a")
        with self.assertRaises(TypeError):
            count_occurrences((1, 2, 1), 1)

    def test_no_forbidden_constructs(self):
        source = inspect.getsource(count_occurrences)
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
            if isinstance(node, ast.Attribute) and node.attr == "count":
                self.fail("list.count() is not allowed.")
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                self.fail("Slicing is not allowed.")


if __name__ == "__main__":
    unittest.main()
