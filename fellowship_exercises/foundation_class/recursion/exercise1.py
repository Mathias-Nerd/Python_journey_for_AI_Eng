#Given a positive integer *N*, write a recursive function to calculate the sum of all integers from *1 to N*, inclusive.


def sum_up_to_n(n):
    if n == 1:
        return n
    return n + sum_up_to_n(n-1)

number = int(input("Enter a positive number: "))
print(f"The sum of natural numbers up to {number} is {sum_up_to_n(number)}")