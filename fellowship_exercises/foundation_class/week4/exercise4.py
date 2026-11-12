#Given a list of numbers and a target number, find the first valid pair whose sum equals the target. Return their indices

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[nums[i]] = i

    return []


print(two_sum([2, 7, 11, 15], 20))