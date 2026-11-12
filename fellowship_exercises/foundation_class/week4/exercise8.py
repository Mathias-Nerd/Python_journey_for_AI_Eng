#Recursive flatten and group
#1. flatten(nested) — take a list that may contain other lists (any depth) and return a flat list of all non-list elements.​
#2. group_by(items, key_fn) — return a dict mapping key_fn(item) → list of items.​
#Then combine: given a nested list of words, flatten it and group by first letter.

def flatten(nested):

    if nested == []:
        return nested

    if isinstance(nested[0], int):
        return [nested[0]] + flatten(nested[1:])
    elif isinstance(nested[0], list):
        return flatten(nested[0]) + flatten(nested[1:])

def group_by(items, key_fn):
    # criteria = set(map(key_fn, items))
    res = {}
    for item in items:
        criteria = key_fn(item)
        if criteria in res:
            res[criteria].append(item)
        else:
            res[criteria] = [item]

    return res


# print(combined([["apple", "avocado"], ["banana"], [["cherry"]]]))
# print(group_by(["apple", "avocado", "banana"], lambda w: w[0]))





# print(flatten([1, [2, [3, [4]], 5]]))

# words = ["apple", "avocado", "banana"]
# res = map(lambda w: w[0], words)
# print(list(res))