"""
Solution for Drill 03: Announce Execution Order
Module: 04-decorators-and-closures
"""


def announce(log_list: list[str]) -> callable:
    """Decorator factory recording decoration and execution lifecycle milestones."""
    def decorator(func: callable) -> callable:
        log_list.append("DECORATION")

        def wrapper(*args, **kwargs):
            log_list.append("BEFORE")
            result = func(*args, **kwargs)
            log_list.append("AFTER")
            return result

        return wrapper
    return decorator
