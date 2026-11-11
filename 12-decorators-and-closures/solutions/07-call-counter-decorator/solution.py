"""
Solution for Drill 07: Call Counter
Module: 04-decorators-and-closures
"""
from functools import wraps


def count_calls(func: callable) -> callable:
    """Decorator tracking execution count via a .calls attribute on wrapper."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
