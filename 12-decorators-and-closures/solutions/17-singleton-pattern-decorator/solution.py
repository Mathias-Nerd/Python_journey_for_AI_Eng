"""
Solution for Drill 17: Singleton Decorator
Module: 04-decorators-and-closures
"""
from functools import wraps


def singleton(cls: type) -> callable:
    """Class decorator enforcing the Singleton pattern."""
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
