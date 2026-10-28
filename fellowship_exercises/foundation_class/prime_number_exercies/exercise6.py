
"""
Task 6: Find the First N Prime Numbers

*Problem*

Given an integer N, find the first N prime numbers, starting from 2.

Print the prime numbers and calculate their sum.

Here, N represents how many primes to find, not the upper limit of the search.

*Examples*

1. Input: N = 5

First 5 prime numbers: [2, 3, 5, 7, 11]
Sum of primes: 28

2. Input: N = 1

First 1 prime number: [2]
Sum of primes: 2

*Constraints*
- Reuse the is_prime(n) function.
- Use a while loop to search for prime numbers.
- Stop when you have found exactly N primes.
- Do not use *sum()*.
- Do not import libraries.
- Do not hardcode the answer.
"""

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input("Input the number of primes: "))
i = 1
res = []
total = 0
count = 0
while count < n:
    if is_prime(i):
        res.append(i)
        total += i
        count += 1
    i += 1
print(f"First {n} prime numbers: {res}\nSum of primes: {total}")