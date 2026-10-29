"""
Unit tests for Drill 01: Countdown Sum
"""
import ast
import inspect
import unittest
from exercise import countdown_sum


class TestCountdownSum(unittest.TestCase):

    def test_standard_odd_inputs(self):
        """Test regular odd integers."""
        self.assertEqual(countdown_sum(1), 1)
        self.assertEqual(countdown_sum(3), 4)    # 3 + 1
        self.assertEqual(countdown_sum(5), 9)    # 5 + 3 + 1
        self.assertEqual(countdown_sum(7), 16)   # 7 + 5 + 3 + 1

    def test_standard_even_inputs(self):
        """Test regular even integers."""
        self.assertEqual(countdown_sum(2), 1)    # 1
        self.assertEqual(countdown_sum(4), 4)    # 3 + 1
        self.assertEqual(countdown_sum(6), 9)    # 5 + 3 + 1
        self.assertEqual(countdown_sum(8), 16)   # 7 + 5 + 3 + 1

    def test_zero_and_negatives(self):
        """Edge cases: zero and negative inputs must return 0."""
        self.assertEqual(countdown_sum(0), 0)
        self.assertEqual(countdown_sum(-1), 0)
        self.assertEqual(countdown_sum(-10), 0)

    def test_type_error_on_invalid_types(self):
        """Ensure non-integer types raise TypeError."""
        with self.assertRaises(TypeError):
            countdown_sum("5")
        with self.assertRaises(TypeError):
            countdown_sum(3.14)
        with self.assertRaises(TypeError):
            countdown_sum([5])

    def test_no_forbidden_constructs(self):
        """Ensure no loops, sum(), or comprehensions are used in the source."""
        source = inspect.getsource(countdown_sum)
        parsed = ast.parse(source)

        for node in ast.walk(parsed):
            self.assertNotIsInstance(
                node, (ast.For, ast.While),
                "Forbidden construct used: loops (for/while) are not allowed!"
            )
            self.assertNotIsInstance(
                node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
                "Forbidden construct used: comprehensions are not allowed!"
            )
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(
                    node.func.id, ["sum"],
                    "Forbidden construct used: built-in sum() is not allowed!"
                )


if __name__ == "__main__":
    unittest.main()
