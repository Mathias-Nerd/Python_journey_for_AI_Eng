"""
Write a recursive function recursive_list_sum(lst) that calculates and returns the sum of all numbers in a list.
"""


def recursive_list(lst):
    if len(lst) < 1:
        return 0
    return lst[0] + recursive_list(lst[1:])


print(recursive_list([1, 2, 3, 4, 5]))
