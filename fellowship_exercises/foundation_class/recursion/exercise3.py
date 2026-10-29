#Given two integers, base and exponent, write a recursive function to calculate the value of base raised to the power of exponent.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 1))