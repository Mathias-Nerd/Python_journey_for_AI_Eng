#Maximum sub array


def max_subarray_brute(nums):
    res = {}
    largest = float("-inf")
    largest_key = 0
    if len(nums) == 1:
        return f"sum {nums[0]} indices (0,0)"
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            new_sub = nums[i:j]
            indices = []
            start, end = i, j-1
            indices.append(start)
            indices.append(end)
            indices = tuple(indices)
            sum = 0
            for num in new_sub:
                sum += num
            if sum > largest:
                largest = sum
                largest_key = indices
            value = [new_sub, sum]
            res[indices] = value
            
    return f"sum {largest} {largest_key}"





nums = [-3, -2, -1]
print(max_subarray_brute(nums))