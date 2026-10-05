#Number 5
#Second largest
print("Welcome to a program that finds the second largest number.")
number = input("Enter a list of number eparated by space: ").split()

def second_largest(nums):
    if len(nums) < 2:
        return("No second largest.")
    else:
        largest = float("-inf")
        second_largest = float("-inf")
        for i in range(len(number)):
            number[i] = int(number[i])
            if number[i] > largest:
                second_largest = largest
                largest = number[i]
            elif number[i] > second_largest and number[i] != largest:
                second_largest = number[i]
        return second_largest

print(second_largest(number))