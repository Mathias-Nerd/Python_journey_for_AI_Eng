"""
Solution for Drill 13: Deprecated Warning
Module: 04-decorators-and-closures
"""
from functools import wraps
import warnings


def deprecated(replacement_name: str | None = None) -> callable:
    """Decorator emitting DeprecationWarning when legacy function is invoked."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = f"Function '{func.__name__}' is deprecated."
            if replacement_name:
                msg += f" Use '{replacement_name}' instead."
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper
    return decorator
