"""
Unit tests for Drill 19: Circuit Breaker
"""
import unittest
from exercise import circuit_breaker


class TestCircuitBreaker(unittest.TestCase):

    def test_circuit_trips_open(self):
        @circuit_breaker(failure_threshold=2)
        def service(succeed=False):
            if not succeed:
                raise ValueError("Down")
            return "UP"

        with self.assertRaises(ValueError):
            service(False) # Fail 1

        with self.assertRaises(ValueError):
            service(False) # Fail 2 -> Trips open

        # Next call blocked without calling service
        with self.assertRaises(RuntimeError):
            service(True)


if __name__ == "__main__":
    unittest.main()
