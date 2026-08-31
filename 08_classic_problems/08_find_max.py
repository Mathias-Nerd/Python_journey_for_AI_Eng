#Name: Mathias.Nerd
# Write a function find_max(lst) that takes a list of numbers and returns the maximum number in the list.
# Do not use the built-in max() function. Implement the logic manually using a loop.
# Examples:
# find_max([1, 5, 3, 9, 2]) -> 9
# find_max([-10, -5, -20]) -> -5
# find_max([7]) -> 7


def find_max(lst):
    if len(lst) == 0: return 
    maxi = lst[0]
    for i in range(1,len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]
    return maxi

print(find_max([1, 5, 3, 9, 2]))
print(find_max([-10, -5, -20]))
print(find_max([7]))
print(find_max([]))