"""
Task 5: Find Prime Numbers Between Two Limits

*Problem*
Given two integers, start and end, determine whether each integer in the interval is prime.
Print all prime numbers in the interval and calculate their sum.
Both limits are inclusive.

*Examples*

1. Input: start = 10, end = 20

Prime numbers between 10 and 20: [11, 13, 17, 19]
Sum of primes: 60

2. Input: start = 14, end = 16

Prime numbers between 14 and 16: []
Sum of primes: 0

*Constraints*

- Reuse the is_prime(n) function.
- Use a while loop to iterate through the interval.
- Use `i * i <= n` when checking potential divisors.
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

start = int(input("Enter start: "))
end = int(input("Enter end: "))
i = start
res = []
sum_of_primes = 0
while i <= end:
    if is_prime(i):
        res.append(i)
        sum_of_primes += i
    i += 1
print(f"Prime numbers between {start} and {end}: {res}")
print(f"Sum of primes: {sum_of_primes}")