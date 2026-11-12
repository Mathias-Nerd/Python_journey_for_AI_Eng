#Given a list of numbers, find the second-largest unique number.

def second_largest(nums: list[int]) -> int:
    largest = float("-inf")
    second_largest = float("-inf")
    for num in nums:
        largest, second_largest = step(largest, second_largest, num)
    
    return second_largest


def step(largest, second_largest, x) -> tuple[int, int]:
    if x > largest:
        largest = x
    if x != largest and x > second_largest:
        second_largest = x

    return largest, second_largest

print(second_largest([4, 9, 8, 2, 9, 7]))