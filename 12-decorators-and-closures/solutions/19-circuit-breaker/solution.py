"""
Solution for Drill 19: Circuit Breaker
Module: 04-decorators-and-closures
"""
from functools import wraps


def circuit_breaker(failure_threshold: int = 3) -> callable:
    """Decorator preventing repeated calls to failing external dependencies."""
    def decorator(func: callable) -> callable:
        failures = 0
        state = "CLOSED"  # CLOSED, OPEN

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal failures, state
            if state == "OPEN":
                raise RuntimeError("Circuit breaker is OPEN: service unavailable")

            try:
                res = func(*args, **kwargs)
                failures = 0
                return res
            except Exception:
                failures += 1
                if failures >= failure_threshold:
                    state = "OPEN"
                raise

        return wrapper
    return decorator
