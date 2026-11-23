#Smallest, Largest and average

def stats(nums):
    if len(nums) == 0: 
        return None
    smallest = float("inf") 
    largest = float("-inf")
    sum = 0
    for num in nums:
        sum += num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    
    average = sum / len(nums)

    return smallest, largest, average


print(stats([4, 9, 2, 7]) )
print(stats([5]) )
print(stats([-3, -1, -2]) )
print(stats([])  )