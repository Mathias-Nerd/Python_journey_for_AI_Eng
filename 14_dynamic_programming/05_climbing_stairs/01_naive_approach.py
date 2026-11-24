#24 - Nov - 2026
#Dynamic programming
#Climbing stairs (Naive approach)
"""
You are climbing a staircase with n steps.
At each move, you can either:
- Climb 1 step.
- Climb 2 steps.
Write a function climbStairs(n) that returns the total number of distinct ways you can reach the top of the staircase."""


def climbing_stairs(n):
    #Base case
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    #REcusive case
    return  climbing_stairs(n-1) + climbing_stairs(n-2)
    

print(climbing_stairs(45))