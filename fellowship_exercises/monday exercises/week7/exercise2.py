#Mathias Nerd
#Week 7 Exercise
#Question 2: Fibonacci sequence
#Print the first N numbers of the Fibonacci sequence. Calculate the sum of only the even numbers in that sequence. Finally, print the sequence in reverse order.
def fibonacci_sequence(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
        exit(0)
    

    if n > 2:
        sum = 0
    #getting all the terms first
        for _ in range(n-2):
            a, b = b, a + b
            if b % 2 == 0:
                sum += b
    j = 0
    while j < n:
        print(b, end=" ")
        b, a = a, b-a
        j += 1
    print()
(fibonacci_sequence(5))
