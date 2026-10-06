#Mathias-Nerd
#Number 7
# Recursive Flatten and Group
"""
Two parts:
1. flatten(nested) — take a list that may contain other lists (any depth) and return a flat list of all non-list elements.
2. group_by(items, key_fn) — return a dict mapping key_fn(item) → list of items.
Then combine: given a nested list of words, flatten it and group by first letter.
"""

def flatten(nested):
    if nested == []:
        return []
    first = nested[0]
    rest = nested[1:]
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    else:
        return [first] + flatten(rest)

print((flatten([1, [2, [3, [4]], 5]])))


"""
group_by(["apple", "avocado", "banana"], lambda w: w[0])
# {'a': ['apple', 'avocado'], 'b': ['banana']}
"""

def group_by(items, key_fn):
    res = {}
    for item in items:
        key = key_fn(item)

        if key not in res:
            res[key] = []

        res[key].append(item)
    return res

print(group_by(["apple", "avocado", "banana"], lambda w: w[0]))

# Then combine: given a nested list of words, flatten it and group by first letter
def combine(nested):
    falttened_word = flatten(nested)
    return group_by(falttened_word, lambda word: word[0])

print(combine(([["apple", "avocado"], ["banana"], [["cherry"]]])))