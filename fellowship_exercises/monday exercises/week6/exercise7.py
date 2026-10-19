#Mathias-Nerd
#Monday exercise: week 6
#Question 7: Find duplicates
# Given a list of numbers, find all the numbers that appear more than once. Print each duplicate only once, in the order it first appears as a duplicate.
def find_duplicates(numbers):
    freq = {}
    result = []
    for item in numbers:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for x, f in freq.items():
        if f > 1 and x not in result:
            result.append(x)
    print(result, end="")
    print(" (no duplicates)" if len(result) == 0 else "") 

numbers = [1, 1, 1, 1]
find_duplicates(numbers)
