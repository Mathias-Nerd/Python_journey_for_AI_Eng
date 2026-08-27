"""
Write a recursive function in Python named power(base, exp) that takes two non-negative integers, base and exp, and calculates $\text{base}^{\text{exp}}$ (i.e., base raised to the power of exp).
"""
# Author: Mathias Nerd


def pow(base, exp):
    if exp < 1:
        return 1
    return base * pow(base, exp - 1)


print(pow(2, 5))
