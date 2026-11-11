"""
Solution for Drill 05: Arguments Forwarder
Module: 04-decorators-and-closures
"""
from functools import wraps


def record_call_args(func: callable) -> callable:
    """Decorator capturing and exposing *args and **kwargs on wrapper attributes."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.last_args = args
        wrapper.last_kwargs = kwargs
        return func(*args, **kwargs)

    wrapper.last_args = None
    wrapper.last_kwargs = None
    return wrapper
