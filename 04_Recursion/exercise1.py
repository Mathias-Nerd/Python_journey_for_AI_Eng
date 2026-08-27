"""
Write a recursive function in Python named sum_up_to(n) that takes a positive integer $n$ and calculates the sum of all integers from $1$ up to $n$.
"""
# Author: Mathias Nerd


def sum_up_to(n):
    if n < 1:
        return 0
    return n + sum_up_to(n-1)


print(sum_up_to(-1))
