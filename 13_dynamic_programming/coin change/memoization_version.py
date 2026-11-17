#17 - 11 - 2026
#Mathias-Nerd
#Dynamic Programming: Coin change problem (Memoization (Top- Down))

"""
You are given an array of coin denominations and an integer amount.
Write an algorithm that returns the minimum number of coins required to make the given amount.
You may use each denomination an unlimited number of times.
If the amount cannot be formed using the available denominations, return -1.
Example
coins = [1, 2, 5]
amount = 11
Output: 3
"""

def coin_change(coins, amount):
    memo = {}

    def solve(rem):
        if rem in memo:
            return memo[rem]

        #base case
        if rem == 0:
            return 0

        if rem < 0:
            return float("inf")

        minimum = float("inf")

        for coin in coins:
            minimum = min(minimum, 1 + solve(rem-coin))

        memo[rem] = minimum

        return minimum

    answer = solve(amount)
    return  answer if answer < float("inf") else -1

        
print(coin_change([1,2, 5], 11))