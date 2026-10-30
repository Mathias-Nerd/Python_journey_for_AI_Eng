"""
Unit tests for Drill 06: Recursive Palindrome Check
"""
import ast
import inspect
import unittest
from exercise import is_palindrome


class TestPalindromeCheck(unittest.TestCase):

    def test_palindromes(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(""))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("Racecar"))  # Case-sensitive

    def test_type_error_on_non_string(self):
        with self.assertRaises(TypeError):
            is_palindrome(12321)
        with self.assertRaises(TypeError):
            is_palindrome(["a", "b", "a"])
        with self.assertRaises(TypeError):
            is_palindrome(None)

    def test_no_forbidden_constructs(self):
        source = inspect.getsource(is_palindrome)
        parsed = ast.parse(source)

        for node in ast.walk(parsed):
            self.assertNotIsInstance(
                node, (ast.For, ast.While),
                "Loops are not allowed."
            )
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, ["reversed"], "reversed() is forbidden.")
            if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Slice):
                self.fail("String slicing is forbidden. Converge using pointer indices.")


if __name__ == "__main__":
    unittest.main()
