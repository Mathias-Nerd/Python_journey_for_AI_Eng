"""
Unit tests for Drill 08: Execution Timer
"""
import time
import unittest
from exercise import time_execution


class TestExecutionTimer(unittest.TestCase):

    def test_duration_measurement(self):
        @time_execution
        def pause():
            time.sleep(0.02)
            return 99

        res = pause()
        self.assertEqual(res, 99)
        self.assertGreaterEqual(pause.last_duration, 0.015)


if __name__ == "__main__":
    unittest.main()
