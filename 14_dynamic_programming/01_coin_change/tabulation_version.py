#17 - 11 - 2026
#Mathias-Nerd
#Dynamic Programming: Coin change problem (Tabulation (Bottom- Up))

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
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount+1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount-coin])
        

    return dp[amount] 

print(coin_change([1,2, 5],11))