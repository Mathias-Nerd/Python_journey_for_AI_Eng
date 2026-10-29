"""
Unit tests for Drill 03: Recursive String Reversal
"""
import ast
import inspect
import unittest
from exercise import reverse_string


class TestReverseString(unittest.TestCase):

    def test_standard_strings(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("python"), "nohtyp")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_single_char_and_empty(self):
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string(""), "")

    def test_palindrome_strings(self):
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("madam"), "madam")

    def test_type_error_on_non_string(self):
        with self.assertRaises(TypeError):
            reverse_string(123)
        with self.assertRaises(TypeError):
            reverse_string(["h", "e", "l", "l", "o"])
        with self.assertRaises(TypeError):
            reverse_string(None)

    def test_no_forbidden_constructs(self):
        source = inspect.getsource(reverse_string)
        parsed = ast.parse(source)

        for node in ast.walk(parsed):
            self.assertNotIsInstance(
                node, (ast.For, ast.While),
                "Loops are not allowed."
            )
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ["reversed"], "reversed() is not allowed.")
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                if node.slice.step is not None:
                    if isinstance(node.slice.step, ast.UnaryOp) or (
                        isinstance(node.slice.step, ast.Constant) and node.slice.step.value == -1
                    ):
                        self.fail("Negative slicing ([::-1]) is not allowed.")


if __name__ == "__main__":
    unittest.main()
