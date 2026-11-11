"""
Drill 02: Closure State Accumulator
Module: 04-decorators-and-closures
"""


def make_accumulator(initial_value: int = 0) -> callable:
    """
    Returns an accumulate function retaining state across calls via nonlocal.
    """
    # TODO: Implement closure with nonlocal accumulator
    def accumulate(delta: int = 1) -> int:
        nonlocal  initial_value

        initial_value += delta
        return initial_value

    return accumulate


acc = make_accumulator(10)

print(acc(5)) 
print(acc(2)) 
print(acc(-10)) 