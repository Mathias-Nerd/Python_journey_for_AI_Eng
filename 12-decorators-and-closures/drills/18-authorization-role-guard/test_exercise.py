"""
Unit tests for Drill 18: Authorization Guard
"""
import unittest
from exercise import require_role


class TestAuthGuard(unittest.TestCase):

    def test_authorized_access(self):
        admin_user = {"role": "admin"}

        @require_role("admin", user_getter=lambda: admin_user)
        def view_secrets(): return "confidential"

        self.assertEqual(view_secrets(), "confidential")

    def test_unauthorized_raises(self):
        guest_user = {"role": "guest"}

        @require_role("admin", user_getter=lambda: guest_user)
        def view_secrets(): return "confidential"

        with self.assertRaises(PermissionError):
            view_secrets()


if __name__ == "__main__":
    unittest.main()
