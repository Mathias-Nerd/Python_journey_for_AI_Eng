# Implementing selection sort
# Author: Mathias Nerd

# Algorithm
# For each position in the array:
# 1. Assume the current position contains the smallest value.
# 2. Search through the remaining unsorted elements.
# 3. If you find something smaller, remember its index.
# 4. Once you've searched everything, swap the smallest value with the value at the current position.
# 5. Move to the next position.
# 6. Repeat until the array is sorted.

def selection_sort(arr):
    print(arr, "Original array")
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"{arr} Pass {i+1}")
    print("_________________________________________")


selection_sort([5, 4, 3, 2, 1])
selection_sort([7, 2, 9, 1, 5, 3, 8])
selection_sort([4, 10, 2, 8, 1, 7, 3, 9, 5, 6])
