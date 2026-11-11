"""
Unit tests for Drill 20: Plugin Registry
"""
import unittest
from exercise import PluginRegistry


class TestPluginRegistry(unittest.TestCase):

    def test_plugin_registration(self):
        reg = PluginRegistry()

        @reg.register("csv")
        def parse_csv(data): return data.split(",")

        self.assertIn("csv", reg.all_plugins())
        self.assertEqual(reg.get("csv")("a,b"), ["a", "b"])

    def test_missing_plugin_raises(self):
        reg = PluginRegistry()
        with self.assertRaises(KeyError):
            reg.get("xml")


if __name__ == "__main__":
    unittest.main()
