"""
Solution for Drill 12: Rate Limiter
Module: 04-decorators-and-closures
"""
from collections import deque
from functools import wraps
import time


def rate_limit(max_calls: int, period_seconds: float) -> callable:
    """Decorator limiting calls to max_calls within a sliding window of period_seconds."""
    def decorator(func: callable) -> callable:
        call_timestamps = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Evict timestamps older than period_seconds
            while call_timestamps and now - call_timestamps[0] >= period_seconds:
                call_timestamps.popleft()

            if len(call_timestamps) >= max_calls:
                raise RuntimeError("Rate limit exceeded")

            call_timestamps.append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator
