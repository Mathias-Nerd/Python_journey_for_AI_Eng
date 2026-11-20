#Mathias-nerd
#Fellowship Monday Exercises
#Week 8 - Exercise 10: Stress test










def memoize(max_size=None):

    def decorator(func):
        cache = {}

        def wrapper(*args, **kwargs):
            if (amount, index) in cache:
                return cache[(amount, index)]
            res = count_way(amount, coins, index)
            
            return res
        return wrapper

    return decorator





def count_way(amount, coins, index=0):
    #Base case
    if amount == 0: return 1
    if amount < 0: return 0
    if index == len(coins): return 0
    res = 0

    #Use coin
    use_coin = count_way(amount-coins[index], coins, index)


    #Skip coin
    skip_coin =  count_way(amount, coins, index+1)

    return use_coin + skip_coin
        
        
    

    
print(count_way(5, [1, 2,3]))
