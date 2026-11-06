#Mathias-Nerd
#week 8 question 1 bonus part

def recursive_binary_search(nums, target, left = 0, right = None, comparison = 0, leftmost = -1):
    if right == None: right = len(nums) - 1

    if left > right:
        return leftmost, comparison

    mid = (left + right) // 2

    comparison += 1
    if target > nums[mid]:
        return recursive_binary_search(nums, target, mid + 1, right, comparison, leftmost)
    elif target < nums[mid]:
        return recursive_binary_search(nums, target, left, mid - 1, comparison, leftmost)
    else:
        leftmost = mid
        return recursive_binary_search(nums, target, left, mid - 1, comparison, leftmost)


print(recursive_binary_search([], 4))