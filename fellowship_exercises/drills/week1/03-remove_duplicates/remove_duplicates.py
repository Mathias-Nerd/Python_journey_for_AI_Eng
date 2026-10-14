def remove_duplicates(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res