#Mathias_nerd
#Fellowship week 4
#Question 9: Memoized fibonacci

# Write a decorator memoize that caches a function's results. Apply it to a recursive Fibonacci function and show that fib(35) runs fast.


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result 
        return result


    return wrapper




@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))
