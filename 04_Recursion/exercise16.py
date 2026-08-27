"""
Write a recursive function binary_search(arr, target, low, high) that searches for a target number inside a sorted list arr and returns its index, or -1 if the number does not exist in the list.
Initialise Right Bound: If right is None, set right = len(lst) - 1.
Base Case 1 (Not Found): If left > right, return -1.
Calculate Mid: mid = (left + right) // 2.
Base Case 2 (Found): If lst[mid] == target, return mid.
Recursive Left Search: If lst[mid] > target, return binary_search(lst, target, left, mid - 1).
Recursive Right Search: If lst[mid] < target, return binary_search(lst, target, mid + 1, right).
"""
def binary_search(arr, target, low=0, high=None):
    if high == None:
        high = len(arr) - 1
    if low > high:  # Basecase1
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid-1)
    else:
        return binary_search(arr, target, mid + 1, high)
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# 1. Standard search (Target in the middle)
print(binary_search(numbers, 23))  # Expected output: 5
# 2. Boundary test (First element)
print(binary_search(numbers, 2))  # Expected output: 0
# 3. Boundary test (Last element)
print(binary_search(numbers, 91))  # Expected output: 9
# 4. Missing element test
print(binary_search(numbers, 15))  # Expected output: -1
# 5. Edge case (Empty list)
print(binary_search([], 5))  # Expected output: -1
