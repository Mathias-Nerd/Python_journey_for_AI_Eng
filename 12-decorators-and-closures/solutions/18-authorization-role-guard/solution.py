"""
Solution for Drill 18: Authorization Guard
Module: 04-decorators-and-closures
"""
from functools import wraps


def require_role(required_role: str, user_getter: callable) -> callable:
    """Decorator checking that user_getter() yields a user with required_role."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = user_getter()
            if not user or user.get("role") != required_role:
                raise PermissionError(f"User lacks required role: {required_role}")
            return func(*args, **kwargs)

        return wrapper
    return decorator
