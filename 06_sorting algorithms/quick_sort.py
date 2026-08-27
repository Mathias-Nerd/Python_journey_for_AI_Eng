#Implementing quick sort algorithm
#Author: Mathias Nerd 24-Aug-2026
def quick_sort(arr):
    #Base case
    if len(arr) <= 1:
        return arr
    #Partitioning
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

print(quick_sort([5,1,9,3,9,1,5,2]))
