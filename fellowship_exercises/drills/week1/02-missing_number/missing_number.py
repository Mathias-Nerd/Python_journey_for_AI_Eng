def find_missing(nums):
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1] - 1:
            return nums[i] + 1