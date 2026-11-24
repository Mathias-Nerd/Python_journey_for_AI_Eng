#24 - Nov - 2026
#Dynamic programming
#Climbing stairs (tabulation approach)
"""
You are climbing a staircase with n steps.
At each move, you can either:
- Climb 1 step.
- Climb 2 steps.
Write a function climbStairs(n) that returns the total number of distinct ways you can reach the top of the staircase."""


def climbing_stairs(n):

    memo = [0] * (n+1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, len(memo)):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

print(climbing_stairs(45))