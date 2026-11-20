#Mathias-Nerd
#20-11-2026
#Dynamic Programming: Can Sum
#Naive recursive approach
"""
Understand the problem
Given an array of numbers and a target sum, determine whether the target can be obtained by adding numbers from the array.
- You can use a number multiple times.
- Return True if the target can be reached.
- Return False otherwise.
"""


def canSum(nums, target):

    #Base case
    if target == 0: return True
    if target < 0: return False

    #Recursive case
    for num in nums:
        res = canSum(nums, target-num)
        if res: return True

    return False

print(canSum([2,4], 9))