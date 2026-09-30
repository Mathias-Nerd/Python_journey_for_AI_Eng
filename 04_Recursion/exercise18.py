#Author: Mathias Nerd
# A recursive function to find the largest number from a list
def find_largest(arr):
    #Base case: This condition is met when the list is empty
    if len(arr) == 0: 
        return "There is no number in the list"

    #Main Base case : This condition is met when there is only one item in the list originally or when the recursive call is at the point of checking the last element in the array 
    if len(arr) == 1: 
        return arr[0]

    #Recursive case
    return arr[0] if (arr[0] > find_largest(arr[1:])) else find_largest(arr[1:])

print(find_largest([3,7,2,9,4]))
print(find_largest([10, 5, 8, 2]))

