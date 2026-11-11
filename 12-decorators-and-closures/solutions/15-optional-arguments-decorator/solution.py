"""
Solution for Drill 15: Optional Arguments Decorator
Module: 04-decorators-and-closures
"""
from collections.abc import Callable
from functools import wraps


def prefix(_func: Callable | None = None, *, tag: str = "INFO") -> Callable:
    """Decorator supporting both @prefix and @prefix(tag='CUSTOM') syntaxes."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f"[{tag}] {res}"

        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)
