"""
Drill 07: Fibonacci with Memoization
Module: 01-recursion
"""


def fibonacci(n: int, memo: dict | None = None) -> int:
    """
    Recursively computes the n-th Fibonacci number using memoization.

    Args:
        n (int): Non-negative integer.
        memo (dict | None): Optional dictionary caching previous results.

    Returns:
        int: The n-th Fibonacci number.

    Raises:
        ValueError: If n < 0.
        TypeError: If n is not an integer.
    """
    # TODO: Implement validation, base cases, memo lookup, and recursive caching
    if n < 0:
        raise ValueError("n must be non-negative")
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if memo == None:
        memo = {}
    if n < 2:
        return n
    if n in memo.keys():
        return memo[n]
    else:
        res =  fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = res
        return res



print(fibonacci(50))