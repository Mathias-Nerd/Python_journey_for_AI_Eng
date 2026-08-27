"""
Level 3 — Exercise 4: Sum of a Deeply Nested List
The Goal: Write a recursive function nested_sum(lst) that calculates the total sum of all numbers inside a list, no matter how deeply nested the sub-lists are.
Initialise a local sum variable: total = 0.
Loop through each item in lst:
If item is a list (isinstance(item, list)), recursively call nested_sum(item) and add the returned number to total.
Otherwise, add item directly to total.
Return total.
"""


def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


print(nested_sum([1, [2, [3, 4]], 5]))  # Returns 15
