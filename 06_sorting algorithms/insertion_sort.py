# Implementing Insertion sort
# Author: Mathias Nerd

# Algorithm
# 1. Start from the .second element because we consider the first element already sorted.
# 2. Take the current element and call it the key.
# 3. Look at the element immediately to the left of the key.
# 4. If that element is larger than the key, move it one position to the right.
# 5. Move one position farther left and repeat the comparison.
# 6. Continue shifting larger elements to the right until:
#    you reach the beginning of the array, or
#    you find an element that is smaller than or equal to the key.
# 7. Insert the key into the empty position created by the shifts.
# 8. Move to the next element and repeat the process.
# 9. When you reach the end of the array, the entire array is sorted.

def insertion_sort(arr):
    print(arr, "Original array")
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"{arr} Pass {i}")


insertion_sort([7, 2, 9, 1, 5, 3])
