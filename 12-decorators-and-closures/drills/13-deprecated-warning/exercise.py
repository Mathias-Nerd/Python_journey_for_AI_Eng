"""
Drill 13: Deprecated Warning Decorator
Module: 04-decorators-and-closures
"""
import warnings
from functools import wraps


def deprecated(replacement_name: str | None = None) -> callable:
    """
    Decorator emitting DeprecationWarning on execution.
    """
    # TODO: Implement deprecation warning emitter
    pass
