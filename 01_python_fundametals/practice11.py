# Two Sum
# #Author: Mathias Nerd 
#Date: 20 Aug 2026
"""
Question: Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
Description: Assume each input has exactly one solution, and you cannot use the same element twice in your sum. You can return the indices in any order.
"""
#Method 1
# def two_sum(nums, target):
#     result = []
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 result.append(i)
#                 result.append(j)
#                 return result
#     return "No answer"


#Method 2
def two_sum(nums, target):
    seen = {}
    for index, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return [seen[remaining], index]
        seen[value] = index


print(two_sum([3,3], 6))