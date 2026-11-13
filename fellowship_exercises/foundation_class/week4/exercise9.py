# 13 - 11 - 2026
#Write a decorator memoize that caches a function's results. Apply it to a recursive Fibonacci function and show that fib(35) runs fast.




def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache.keys():
            cache[args] = func(*args)
            return cache[args]
        else:
            return cache[args]

    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

print(fib(35))
