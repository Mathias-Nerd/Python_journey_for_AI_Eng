"""
Drill 11: Retry on Exception
Module: 04-decorators-and-closures
"""
from functools import wraps


def retry(max_attempts: int = 3, exceptions: tuple = (Exception,)) -> callable:
    """
    Parametric decorator retrying execution up to max_attempts on caught exceptions.
    """
    # TODO: Implement retry loop
    pass
