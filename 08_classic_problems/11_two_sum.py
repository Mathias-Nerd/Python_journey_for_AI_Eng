#Author: Mathias.Nerd
# Write a function two_sum(nums, target) that takes a list of integers nums and an integer target, and returns the indices of the two numbers that add up to target.
# Assume each input has exactly one solution, and you may not use the same element twice.
def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], index]
        else:
            seen[value] = index

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))