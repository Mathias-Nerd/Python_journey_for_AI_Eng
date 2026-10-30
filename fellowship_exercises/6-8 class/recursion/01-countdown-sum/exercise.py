"""
Drill 01: Countdown Sum of Odd Integers
Module: 01-recursion
"""


def countdown_sum(n: int) -> int:
    """
    Recursively returns the sum of odd positive integers from n down to 1.

    Args:
        n (int): Starting integer.

    Returns:
        int: Sum of odd positive integers <= n.

    Raises:
        TypeError: If n is not an integer.

    Constraints:
        - Must be purely recursive.
        - No loops (for / while).
        - No sum(), count(), or comprehensions.
    """
    # TODO: Implement type validation, base cases, and recursive step
    if not isinstance(n, int):
        raise TypeError("Wrong type.")
    if n <= 0:
        return 0
    if n % 2 == 0:
        n -= 1
    return n + countdown_sum(n-2)

