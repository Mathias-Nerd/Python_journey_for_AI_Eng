""""
Write a recursive function in Python named fibonacci(n) that returns the $n$-th number in the Fibonacci sequence.
"""
# Author: Mathias Nerd


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)


print(fib(6))
