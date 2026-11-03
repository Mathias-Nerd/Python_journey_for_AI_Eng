#Binary search
#Given a sorted list of integers and a target, return the index of the first (leftmost) occurrence of the target, or -1 if it is not present. Also return how many comparisons your search made.

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    count = 0
    index = 0
    while low <= high:
        mid = (low + high + 1) // 2
        if nums[mid] < target:
            high = mid - 1
        elif nums[mid] > target:
            low = mid + 1
        if nums[mid] == target:
            index = mid
            high = mid - 1
        count += 1
    if len(nums) == 0:
        return -1, 0
    elif index == 0:
        return -1, count
    return index, count


    
print(binary_search([1, 3, 3, 3, 5, 8], 3))
print(binary_search([], 3))
    