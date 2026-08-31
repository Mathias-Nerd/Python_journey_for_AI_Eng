#Author: Mathias.Nerd
# Write a function fibonacci(n) that returns the nth Fibonacci number.
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
# fibonacci(0)=0, fibonacci(1)=1


#Iterative version
def fibonacci(n):
    if n == 0:
            return 0
    a = 0
    b = 1
    for i in range(1, n + 1):
        a, b= b, a + b
    return a

#Recursive version
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-2) + fib(n-1)

print(fibonacci(0))