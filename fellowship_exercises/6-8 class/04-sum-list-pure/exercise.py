"""
Drill 04: Pure Recursive List Sum
Module: 01-recursion
"""


def sum_list(numbers: list[int | float], index: int = 0) -> int | float:
    """
    Recursively sums a list of numbers using an index pointer.

    Args:
        numbers (list): List of integers or floats.
        index (int): Current position in the list.

    Returns:
        int | float: The sum of elements.

    Raises:
        TypeError: If numbers is not a list.
    """
    # TODO: Implement validation, base case, and index-based recursive step
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if index >= len(numbers):
        return 0
    return numbers[index] + sum_list(numbers, index + 1)
numbers = [4.5, 2.5]
print(sum_list(numbers))
