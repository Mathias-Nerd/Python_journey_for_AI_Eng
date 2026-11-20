
#Mathias-Nerd
#Dynamic programming
#The Naive Recursion A pproach

"""
Write count_ways(amount, coins) that returns the number of different combinations of coins that 
make up amount. Order does not matter: 1+2 and 2+1 count as one way. Coins can be reused. 
count_ways(5, [1, 2, 5])         → 4 
count_ways(10, [2, 5, 3, 6])     → 5 
count_ways(0, [1, 2])            → 1     # one way to make nothing: use no coins 
count_ways(3, [2])               → 0 
count_ways(100, [1, 5, 10, 25, 50]) → 292 
•  Must be recursive (use a helper such as count_ways(amount, coins, index) if you need 
one). 
•  The naive version must make no use of caching. Run it on count_ways(100, [1, 5, 10, 25, 
50]) and notice how much work it does.
"""

def count_way(amount, coins, index=0):
    #Base case
    if amount == 0: return 1
    if amount < 0: return 0
    if index == len(coins): return 0

    #Use coin
    use_coin = count_way(amount-coins[index], coins, index) #uses the curren coin


    #Skip coin
    skip_coin =  count_way(amount, coins, index+1) #skips the current coin and uses the next coin

    return use_coin + skip_coin
        
        