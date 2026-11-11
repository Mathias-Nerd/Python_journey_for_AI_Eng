"""
Solution for Drill 08: Execution Timer
Module: 04-decorators-and-closures
"""
from functools import wraps
import time


def time_execution(func: callable) -> callable:
    """Decorator measuring elapsed execution duration in seconds via time.perf_counter()."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        wrapper.last_duration = time.perf_counter() - start
        return result

    wrapper.last_duration = 0.0
    return wrapper
