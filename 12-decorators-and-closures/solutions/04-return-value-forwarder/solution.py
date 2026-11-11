"""
Solution for Drill 04: Return Value Forwarder
Module: 04-decorators-and-closures
"""
from functools import wraps


def forward_result(func: callable) -> callable:
    """Decorator that executes the wrapped function and returns its result unchanged."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
