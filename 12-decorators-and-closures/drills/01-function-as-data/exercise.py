"""
Drill 01: Functions as First-Class Citizens
Module: 04-decorators-and-closures
"""

from functools import  wraps


def make_multiplier(factor: int) -> callable:
    """
    Returns a function that multiplies its argument by factor.
    """
    # TODO: Implement closure returning inner multiplier function

    def closure(arg):
        return arg * factor


    return closure

double = make_multiplier(2)
    


def apply_pipeline(data: list[int], operations: list[callable]) -> list[int]:
    """
    Applies a sequence of functional operations to each element in data.
    """
    # TODO: Pipe each element through operations list
    
    current = data
    for operation in operations:
        temp = []

        for item in current:
            temp.append(operation(item))

        current = temp

    return current
def add_ten(x): return x + 10
print(apply_pipeline([1,2,3], [double, add_ten]))

# print(data)