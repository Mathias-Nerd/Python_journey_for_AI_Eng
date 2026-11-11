"""
Drill 15: Optional Arguments Decorator
Module: 04-decorators-and-closures
"""
from collections.abc import Callable
from functools import wraps


def prefix(_func: Callable | None = None, *, tag: str = "INFO") -> Callable:
    """
    Decorator usable with or without arguments: @prefix or @prefix(tag="...").
    """
    # TODO: Implement dual-mode decorator detection
    pass
