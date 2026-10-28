"""
Task 2: Sum of Non-Prime Numbers

*Problem*

Given an integer N, determine whether N is prime. Then, find all non-prime integers between 2 and N, inclusive, and calculate their sum.
For this task, a non-prime number is an integer greater than 1 that is not prime.

*Examples*

1. Input: N = 10

10 is not prime.
Non-prime numbers up to 10: [4, 6, 8, 9, 10]
Sum of non-prime numbers: 37
Input: N = 7

2. 7 is prime.
Non-prime numbers up to 7: [4, 6]
Sum of non-prime numbers: 10

*Constraints*
- Reuse your is_prime(n) function.
- Use a loop to examine integers from 2 to N.
- Use an if statement to identify non-prime numbers.
- Maintain a running total without using sum().
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
total = 0
while i <= n:
    if not is_prime(i):
        result.append(i)
        total += i
    i += 1

print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")
print(f"Non-prime numbers up to {n}: {result}")
print(f"Sum of non-prime numbers: {total}")