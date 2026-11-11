"""
Solution for Drill 14: Decorator with Arguments
Module: 04-decorators-and-closures
"""
from functools import wraps


def repeat(num_times: int) -> callable:
    """Decorator factory creating a decorator that executes the wrapped function num_times."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = None
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res

        return wrapper
    return decorator
