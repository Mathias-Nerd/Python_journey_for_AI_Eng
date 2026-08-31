#Name: Mathias.Nerd
# Write a function remove_duplicates(lst) that takes a list lst and returns a new list with all duplicates removed, while keeping the original order of elements.
# Do not use set() directly to remove duplicates, because set does not preserve order in older Python versions.
# Examples:
# Code
# remove_duplicates([1, 2, 2, 3, 4, 4, 5]) -> [1, 2, 3, 4, 5]
# remove_duplicates(['a', 'b', 'a', 'c', 'b']) -> ['a', 'b', 'c']
# remove_duplicates([5, 5, 5, 5]) -> [5]

def remove_duplicates(lst):
    res = []
    for i in lst:
        if i in res:
            continue
        else:
            res.append(i)
    return res

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(['a', 'b', 'a', 'c', 'b']))
print(remove_duplicates([5, 5, 5, 5]))