#Write a recursive program returning the lowest umber in a least
def lowest_num(lst):
    if len(lst) == 0:
        return "No string"
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] < lowest_num(lst[1:]) else lowest_num(lst[1:])


print(lowest_num([4,2,3]))