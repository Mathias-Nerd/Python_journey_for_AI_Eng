#Mathias-Nerd
# Week 4: Question 1
#Given a list of numbers, find the smallest number, largest number, total, and average without using built-in shortcuts for these calculations.
"""
Use this starting list: numbers = [12, 5, 27, 8, 14].
Examples
Input list: [12, 5, 27, 8, 14]
Smallest: 5
Largest: 27
Total: 66
Average: 13.2
"""
numbers = [12, 5, 27, 8, 14]
# numbers = [3, 15, 25, 16, 2, 5]
largest = float("-inf")
smallest = float("inf")
sum = 0
for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    sum += number
avg = sum / len(numbers)
print(f"Smallest: {smallest}\nLargest: {largest}\nTotal: {sum}\nAverage: {avg:.1f}")
