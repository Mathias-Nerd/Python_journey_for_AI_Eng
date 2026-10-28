#Mathias Nerd
#Week 7 Exercise
#Question 3: Given a positive integer, convert it to its binary representation.

def decimal_to_binary(n):
    res = ""
    while n > 0:
        rem  = n % 2
        n = n // 2
        res = str(rem) + res
    return res 

print(decimal_to_binary(25))