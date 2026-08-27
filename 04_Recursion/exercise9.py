"""
The Goal: Write a recursive function recursive_sum(n) that calculates and returns the sum of all integers from n down to 1.
"""
# Author: Mathias Nerd


def recursive_sum(n):
    if n < 1:
        return 0
    return n + recursive_sum(n-1)


print(recursive_sum(3))
