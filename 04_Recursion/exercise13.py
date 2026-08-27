"""
Write a recursive function find_max(lst) that returns the largest number in a list of integers.
"""


def find_max(lst):
    if len(lst) < 1:
        return "Your list doesn't contain a number"
    if len(lst) == 1:
        return lst[0]
    max_from_prev_list = find_max(lst[1:])
    # lst[0] > max_from_prev_list return lst[0]
    return max_from_prev_list if max_from_prev_list > lst[0] else lst[0]


print(find_max([]))
