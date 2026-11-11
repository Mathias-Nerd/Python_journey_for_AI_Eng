"""
Unit tests for Drill 13: Deprecated Warning
"""
import unittest
import warnings
from exercise import deprecated


class TestDeprecated(unittest.TestCase):

    def test_warning_emitted(self):
        @deprecated(replacement_name="safe_func")
        def legacy(): return 42

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            val = legacy()
            self.assertEqual(val, 42)
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
            self.assertIn("legacy", str(w[-1].message))
            self.assertIn("safe_func", str(w[-1].message))


if __name__ == "__main__":
    unittest.main()
