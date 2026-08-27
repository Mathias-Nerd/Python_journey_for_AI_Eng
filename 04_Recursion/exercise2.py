"""
Write a recursive function in Python named sum_of_digits(n) that takes a non-negative integer n and returns the sum of all its individual digits.
1"""
# Author: Mathias Nerd


def sum_of_digits(n):
    if n < 10:
        return n
    last_digit = n % 10
    remaining_digit = n // 10
    return last_digit + sum_of_digits(remaining_digit)


print(sum_of_digits(1234))
print(sum_of_digits(14))
