"""
Solution for Drill 06: Metadata Preserver
Module: 04-decorators-and-closures
"""
from functools import wraps


def logged(func: callable) -> callable:
    """Decorator preserving function identity and metadata using @functools.wraps."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
