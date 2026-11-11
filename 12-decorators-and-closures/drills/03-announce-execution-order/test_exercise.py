"""
Unit tests for Drill 03: Announce Execution Order
"""
import unittest
from exercise import announce


class TestAnnounceExecutionOrder(unittest.TestCase):

    def test_lifecycle_milestones(self):
        events = []

        @announce(events)
        def greet(name):
            events.append(f"GREET {name}")
            return f"Hello, {name}!"

        # Check decoration happened immediately
        self.assertEqual(events, ["DECORATION"])

        # Call function
        ans = greet("World")
        self.assertEqual(ans, "Hello, World!")
        self.assertEqual(events, ["DECORATION", "BEFORE", "GREET World", "AFTER"])


if __name__ == "__main__":
    unittest.main()
