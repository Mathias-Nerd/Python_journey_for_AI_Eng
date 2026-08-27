"""
The Goal: Write a recursive function print_countup(n) that prints numbers from 1 up to n.
"""
# Author: Mathias Nerd


def print_countup(n):
    if n <= 0:
        return
    print_countup(n-1)
    print(n)


print_countup(3)


