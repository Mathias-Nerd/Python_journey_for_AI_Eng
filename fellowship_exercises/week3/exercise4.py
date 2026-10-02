#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 4: Second largest
#Given a list of numbers, find the second-largest unique number.

print("Welcome to a program that finds the second largest number.")
number = input("Enter a list of number eparated by space: ").split()

if len(number) < 2:
    print("No second largest.")
else:
    largest = float("-inf")
    second_largest = float("-inf")
    # print(largest, second_largest)
    # print(number)
    for i in range(len(number)):
        number[i] = int(number[i])
        if number[i] > largest:
            second_largest = largest
            largest = number[i]
        elif number[i] > second_largest and number[i] != largest:
            second_largest = number[i]
    print(second_largest)


