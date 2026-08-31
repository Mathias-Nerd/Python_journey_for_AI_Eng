#Author: Mathias.Nerd
#Write a function factorial(n) that returns the factorial of n

def factorial(n):
    if n < 0:
        return "Invalid NUmber"
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(-1))
print(factorial(5))