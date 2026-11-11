"""
Unit tests for Drill 06: Metadata Preserver
"""
import unittest
from exercise import logged


class TestMetadataPreserver(unittest.TestCase):

    def test_metadata_preserved(self):
        @logged
        def sample_function():
            """This is a docstring."""
            return 42

        self.assertEqual(sample_function.__name__, "sample_function")
        self.assertEqual(sample_function.__doc__, "This is a docstring.")
        self.assertEqual(sample_function(), 42)


if __name__ == "__main__":
    unittest.main()
