"""
Solution for Drill 11: Retry on Exception
Module: 04-decorators-and-closures
"""
from functools import wraps


def retry(max_attempts: int = 3, exceptions: tuple = (Exception,)) -> callable:
    """Decorator retrying flaky function calls up to max_attempts on caught exceptions."""
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
            raise last_err

        return wrapper
    return decorator
