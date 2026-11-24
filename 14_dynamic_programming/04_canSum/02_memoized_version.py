#Mathias-Nerd
#20-11-2026
#Dynamic Programming: Can Sum
#Memoisation approach
"""
Understand the problem
Given an array of numbers and a target sum, determine whether the target can be obtained by adding numbers from the array.
- You can use a number multiple times.
- Return True if the target can be reached.
- Return False otherwise.
"""


def canSum(nums, target, memo = None):
    if memo is None: memo = {}
    if target in memo:
        return memo[target]
    
    #Base case
    if target == 0: return True
    if target < 0: return False

    #Recursive case
    for num in nums:
        res = canSum(nums, target-num, memo)
        if res: 
            memo[target] = res
            return True

    memo[target] = res
    return False

print(canSum([3, 5], 7))