"""
Python Practice: Prime Numbers and Loop Logic
Task 1: Prime Number Counter

Suggested time: 10–12 minutes | Difficulty: Easy
*Problem*

Given an integer N, determine whether N is prime. Then, find and print the number of prime numbers between 2 and N, inclusive.

*Examples*
1. Input: N = 10
10 is not prime.
Primes up to 10: [2, 3, 5, 7]
Number of primes: 4
Input: N = 7

2. 7 is prime.
Primes up to 7: [2, 3, 5, 7]
Number of primes: 4
Constraints

Write a function called `is_prime(n)` to check primality.
- Use a while loop to check potential divisors.
- Stop checking divisors when i * i > n.
- Do not use *sum()*.
- Do not import libraries.
- Do not hardcode the answer.
"""

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input("Enter a number: "))
result = []
i = 2
while i <= n:
    if is_prime(i):
        result.append(i)
    i += 1

print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")
print(f"Primes up to {n}: {result}")
print(f"Number of primes: {len(result)}")