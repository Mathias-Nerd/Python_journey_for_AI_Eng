#FIZZBUZZ
#Author: Mathias Nerd 
#Date: 20 Aug 2026
#Write a function that takes a positive integer $n$ and returns an array or list of strings representing the counting sequence from $1$ up to $n$.
def fizzbuzz(n):
    result = []
    if not(1 <= n <= 10**4):
        return("Invalid number")
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return(result)
            
        

print(fizzbuzz(15))
