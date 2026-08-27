# Implementing merge sort
# Author: Mathias Nerd 24-Aug-2026
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Recursively merge sorting each half of the array
    # Dividing the array into 2 halves
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Store the two sorted arrays
    left_sorted = merge_sort(left_arr)
    right_sorted = merge_sort(right_arr)

    # Now merge the two sorted arrays
    return merge(left_sorted, right_sorted)


# The merge function
def merge(arr1, arr2):
    result = []
    i = 0  # left index
    j = 0  # right index

    # Comparing while there are still elements in both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


# Test Case
if __name__ == "__main__":
    # A completely scrambled list of numbers
    unsorted_list = [38, 27, 43, 3, 9, 82, 10, 19, -5, 0]
    
    print("Original list: ", unsorted_list)
    
    # Running your merge_sort implementation
    sorted_list = merge_sort(unsorted_list)
    
    print("Sorted list:   ", sorted_list)
