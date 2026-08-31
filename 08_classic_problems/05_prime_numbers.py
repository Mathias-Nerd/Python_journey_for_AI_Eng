#Name: Mathias.Nerd
# Write a function is_prime(n) that returns True if n is a prime number, else False.
# Prime is >1 and divisible only by 1 and itself.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    i = 2
    while  i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(17))
print(is_prime(1))
print(is_prime(0))