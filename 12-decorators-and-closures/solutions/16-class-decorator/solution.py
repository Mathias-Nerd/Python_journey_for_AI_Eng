"""
Solution for Drill 16: Class Decorator
Module: 04-decorators-and-closures
"""


def add_repr(cls: type) -> type:
    """Class decorator dynamically generating a clean __repr__ from instance attributes."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{cls.__name__}({attrs})"

    cls.__repr__ = __repr__
    return cls
