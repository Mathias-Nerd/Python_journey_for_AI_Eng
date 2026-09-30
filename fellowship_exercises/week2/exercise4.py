#Fellowship exercise
#Week 2
#Second largest

numbers = input("Enter a list of numbers separated by spaces: ").split()
# numbers = [10, 5, 8, 20, 15] 
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
# nums = [int(i) for i in numbers]
# print(nums)
print(numbers)

#Using a bubble sort to arrange then pick the second from the back
for i in range(0, len(numbers)- 1):
    for j in range(0, len(numbers)- i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # print(numbers)
print(f"The second largest number is: {numbers[-2]}")
