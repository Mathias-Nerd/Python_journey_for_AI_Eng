#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 7: Two sum
#Given a list of numbers and a target number, find the first valid pair of numbers whose sum equals the target. Return their indices (positions). 


print("Welcome to two sum program.")
numbers = input("Enter a list of numbers separated by space: ").split()
target = int(input("Enter target: "))
checked_numbers = {}
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    diff = target - numbers[i]
    if diff in checked_numbers:
        print(f"{checked_numbers[diff]}, {i}")
        break
    else:
        checked_numbers[numbers[i]] = i


