"""
Drill 12: Rate Limiter Decorator
Module: 04-decorators-and-closures
"""
import time
from functools import wraps


def rate_limit(max_calls: int, period_seconds: float) -> callable:
    """
    Parametric decorator restricting calls to max_calls per period_seconds.
    """
    # TODO: Implement sliding window timestamp rate limiter
    pass
