#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 3: Max sub array


#The Brute Force A pproach
def max_subarray_brute(nums):
    """
    This returns the sum, start, and end of a contiguous slice in O(n^2) time
    """
    if len(nums) == 0:
        return None

    max_sum = nums[0]
    best_start = 0
    best_end = 0

    for start in range(0, len(nums)):
        current_sum = 0

        for end in range(start, len(nums)):
            current_sum += nums[end]

            if current_sum > max_sum:
                max_sum = current_sum
                best_start = start
                best_end = end

    return f"sum {max_sum}, indices ({best_start}, {best_end})"




#The Optimal version (Kadane's Algorithm)
def max_subarray_fast(nums):
    """
    This returns the sum, start, and end of a contiguous slice in O(n) time
    """  
    if len(nums) == 0:
        return None

    max_sum = nums[0]
    current_sum = nums[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(nums)):
        if nums[i] > (current_sum + nums[i]):
            current_sum = nums[i]
            start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

    return f"sum {max_sum}, indices ({best_start}, {best_end})"

    





print(max_subarray_brute([-3, -1, -2]))
print(max_subarray_fast([-3, -1, -2]))
