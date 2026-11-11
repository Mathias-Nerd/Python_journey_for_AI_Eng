"""
Drill 18: Role-Based Authorization Guard
Module: 04-decorators-and-closures
"""
from functools import wraps


def require_role(required_role: str, user_getter: callable) -> callable:
    """
    Parametric decorator validating user permissions before function execution.
    """
    # TODO: Implement role-based authorization check
    pass
