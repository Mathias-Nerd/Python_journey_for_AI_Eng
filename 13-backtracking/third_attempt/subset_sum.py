def can_sum(nums, target, i=0):

    
    #Base case
    if i == len(nums):
        return True if target == 0 else False

    #Recursive case

    #include
    target -= nums[i] #choice 1
    res = can_sum(nums, target, i+1) #explore(recurse)
    if res: return True

    #exclude
    target += nums[i] #Backtrack (undo)
    res = can_sum(nums, target, i+1) #explore(recurse)
    if res: return True


    return False

print(can_sum([-3, 4, 5],  3))