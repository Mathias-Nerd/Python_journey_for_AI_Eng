"""
Task 3: Find the Largest Prime Number

*Problem*

Given an integer N, determine whether N is prime. Then, find the largest prime number less than or equal to N.

If no prime number exists within the specified range, report that no prime number was found.

*Examples*

1. Input: N = 10

10 is not prime.
Largest prime up to 10: 7

2. Input: N = 13

13 is prime.
Largest prime up to 13: 13

3. Input: N = 1

1 is not prime.
No prime number found.

*Constraints*

- Use a function called is_prime(n).
- Use a while loop to check potential divisors.
- Do not use *max()*.
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
print(f"No prime number found." if len(result) == 0 else f"Largest prime up to {n}: {result[-1]}")