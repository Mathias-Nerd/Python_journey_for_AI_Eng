#Mathias Nerd
#Week 7 Exercise
#Question 1: Prime number checker
#Given an integer N, determine if it is a prime number. Then, print the sum of all prime numbers from 2 up to N.
"""
Constraints
●​ You may not use range() to iterate from 2 to N directly for the primality check. You must use a while loop.
●​ To check if a number is prime, stop checking divisors at its square root (use i * i <= num without importing
math).
●​ Do not use sum().
●​ Do not import libraries.
●​ Do not hardcode the answer.
"""
def is_prime(num):
    if num < 2:
        return False, f"{num} is not prime"
    i = 2
    while  i * i <= num:
        if num % i == 0:
            return False, f"{num} is not prime"
        i += 1
    return True, f"{num} is prime"

def listing_prime(num):
    result = []
    sum = 0
    i = 2
    while i <= num:
        prime, _ = is_prime(i)

        if prime:
            result.append(i)
            sum += i
        i += 1
    return f"Primes up to {num}: {result}\nSum of primes: {sum}"

def prime_number_checker(num):
    _, prime = is_prime(num)
    numbers_up_to = listing_prime(num)
    return f"{prime}\n{numbers_up_to}"

print(prime_number_checker(7))
    