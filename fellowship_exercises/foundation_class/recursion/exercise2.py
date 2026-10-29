#The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding numbers.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


number = int(input("Enter a positive number: "))
print(f"The Fibonacci number at position {number} is {fibonacci(number)}")
