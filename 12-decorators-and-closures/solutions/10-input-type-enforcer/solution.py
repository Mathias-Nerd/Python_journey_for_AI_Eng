"""
Solution for Drill 10: Input Type Enforcer
Module: 04-decorators-and-closures
"""
from functools import wraps


def enforce_types(*expected_types) -> callable:
    """Decorator enforcing argument types at runtime."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for val, exp_type in zip(args, expected_types):
                if exp_type is int and isinstance(val, bool):
                    raise TypeError(f"Expected int, got bool")
                if not isinstance(val, exp_type):
                    raise TypeError(f"Expected {exp_type.__name__}, got {type(val).__name__}")
            return func(*args, **kwargs)

        return wrapper
    return decorator
