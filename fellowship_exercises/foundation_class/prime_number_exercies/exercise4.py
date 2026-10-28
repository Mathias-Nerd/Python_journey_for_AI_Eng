"""
Task 4: Count the Divisors of a Number
*Problem*

Given an integer N, determine whether N is prime. Then, count the positive divisors of N.
A divisor is a number that divides another number without leaving a remainder.
*Examples*
1. Input: N = 7
7 is prime.
Divisors of 7: [1, 7]
Number of divisors: 2

2. Input: N = 12
12 is not prime.
Divisors of 12: [1, 2, 3, 4, 6, 12]
Number of divisors: 6

*Constraints*
- Use a while loop to find the divisors.
- Use the modulo operator `%` to determine whether a number divides N evenly.
- Do not use *len()* to count the divisors.
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
print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")
res = []
count = 0
i = 1
while i <= n:
    if n % i == 0:
        res.append(i)
        count += 1
    i += 1
print(f"Divisors of {n}: {res}")
print(f"Number of divisors: {count}")

