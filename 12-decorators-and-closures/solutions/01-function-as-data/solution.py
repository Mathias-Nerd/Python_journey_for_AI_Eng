"""
Solution for Drill 01: Functions as First-Class Citizens
Module: 04-decorators-and-closures
"""


def make_multiplier(factor: int) -> callable:
    """Returns a new function that multiplies its argument by factor."""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier


def apply_pipeline(data: list[int], operations: list[callable]) -> list[int]:
    """Applies a sequence of transform functions in order to each item in data."""
    result = []
    for item in data:
        curr = item
        for op in operations:
            curr = op(curr)
        result.append(curr)
    return result
