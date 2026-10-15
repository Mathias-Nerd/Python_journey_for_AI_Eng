#Fellowship exercise
#Week 2
#Two sum
#Given a list of numbers and a target number, find two numbers whose sum equals the target. Return the first valid pair you find.

# numbers =  [2,7, 11, 15]  
# numbers = [3, 8, 4, 6]
numbers = input("Enter a list of numbers separated by spaces: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
target = int(input("Target: "))
res = {}
def two_sum(numbers, target):
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in res:
            return(f"{diff} + {numbers[i]} = {target}")
            # return f"{res[diff]}, {i}"
        else:
            res[numbers[i]] = i

print(two_sum(numbers, target))