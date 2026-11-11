"""
Unit tests for Drill 05: Arguments Forwarder
"""
import unittest
from exercise import record_call_args


class TestArgsForwarder(unittest.TestCase):

    def test_positional_and_kwargs(self):
        @record_call_args
        def format_user(uid, role="member", active=True):
            return f"{uid}:{role}:{active}"

        ans = format_user(101, role="admin", active=True)
        self.assertEqual(ans, "101:admin:True")
        self.assertEqual(format_user.last_args, (101,))
        self.assertEqual(format_user.last_kwargs, {"role": "admin", "active": True})


if __name__ == "__main__":
    unittest.main()
