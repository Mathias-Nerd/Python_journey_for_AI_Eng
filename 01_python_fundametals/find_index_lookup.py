"""
Implement get_item(items, index). Return the item at the given index. If the index is outside the list, return Index out of range. Negative indexes should also return Index out of range for this challenge.
"""

def get_item(items, index):
    # Bug to fix: invalid indexes should not crash the program.
    if index >= len(items) or index <  -(len(items)):
        return "Index out of range"
    return items[int(index)]
