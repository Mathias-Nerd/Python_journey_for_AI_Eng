"""
The Goal: Write a recursive function flatten(lst) that takes a list containing deeply nested sub-lists and returns a single flat list.
Requirements:
Do not use third-party libraries or built-in flattening methods.
You can use a for loop to iterate over elements in the current list layer, but any item that is itself a list must be processed recursively.
Logic: Check each element with isinstance(item, list):
If it is a list, recursively call flatten(item) and extend your result with the returned items.
If it is a standard value (integer/string), append it directly to your result list.
"""
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            # Recursively flatten the sub-list and extend our result
            result.extend(flatten(item))
        else:
            # Append standard items directly
            result.append(item)
    return result


print(flatten([1, [2, [3, 4], 5], 6, [7]]))
