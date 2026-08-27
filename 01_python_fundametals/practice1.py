# write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
def func1(num1, num2):
    if (num1 * num2) <= 1000:
        return num1 * num2
    else:
        return num1 + num2


print(func1(40, 30))
