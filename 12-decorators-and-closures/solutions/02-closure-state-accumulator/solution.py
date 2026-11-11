"""
Solution for Drill 02: Closure State Accumulator
Module: 04-decorators-and-closures
"""


def make_accumulator(initial_value: int = 0) -> callable:
    """Returns an accumulator function that retains a private running total."""
    total = initial_value

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate
