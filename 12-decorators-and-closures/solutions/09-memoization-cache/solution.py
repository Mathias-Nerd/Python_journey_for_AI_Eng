"""
Solution for Drill 09: Memoization Cache
Module: 04-decorators-and-closures
"""
from functools import wraps


def memoize(func: callable) -> callable:
    """Decorator caching pure function return values by argument signature."""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Construct hashable key from positional and sorted keyword arguments
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper
