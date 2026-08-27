# Implementing bubble sorting algorithm
# Author: Mathias Nerd
"""
Bubble Sort in words
Start with the array.
Look at the first two neighboring elements.
Compare them.
If the left one is bigger than the right one, swap them.
If they're already in the correct order, leave them alone.
Move one position to the right and compare the next pair.
Keep doing this until you reach the end of the unsorted portion of the array.
At the end of one complete pass, the largest unsorted element will have moved to the end of the array.
Start another pass, but don't bother checking the element that just reached the end because it's already in its correct position.
Keep repeating this process, making the area you need to check smaller after each pass.
At the beginning of each pass, keep track of whether you made any swaps.
If you complete a whole pass and make zero swaps, that means everything is already in the correct order.
Stop early and return the sorted array.
"""
def bubble_sort(array):
    print(array, "Original array")
    n = len(array)
    # The loop that determines the number of passes
    for i in range(n-1):
        # The begining of every pass
        swapped = False
        # The loop that does the checking and swapping in each pass
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        print(f"{array} Pass {i+1}")
        if swapped == False:
            print("Array is already sorted")
            print("__________________________________________")

            return
    print("__________________________________________")


bubble_sort([1, 2, 3, 5, 8])  # Expected to print "Array is already sorted"
bubble_sort([5, 4, 3, 2, 1])
bubble_sort([7, 2, 9, 1, 5, 3, 8])
bubble_sort([4, 10, 2, 8, 1, 7, 3, 9, 5, 6])
