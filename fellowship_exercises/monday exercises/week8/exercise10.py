#Mathias-nerd
#Fellowship MOnday Exercises
#Week 8 - Exercise 10: Stress test

def count_ways(amount, coins):

    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    for coin in coins:
        amount -= coin
        candidate = 1 + count_ways(amount, coins)
        minimum = candidate if candidate < minimum else minimum
        

    return minimum

print(count_ways(2, [1,2]))