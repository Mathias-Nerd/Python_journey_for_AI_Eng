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

    arr = [float("inf")] * (amount+1)
    arr[0] = 0

    for i in range(1, amount+1):
        # arr[i] = float(("inf"))
        for coin in coins:
            if coin <= i:
                arr[i] = min(arr[i], 1 + arr[i-coin])
                # amount -= coin




    return arr[amount]

print(coin_change([1,2, 5],11))