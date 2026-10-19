#Mathias-Nerd
#MOnday exercise: week 6
#Question 1: List Analyser — Extended
#Given a list of numbers, find the smallest, largest, total, and average — and also report the index of the smallest and largest values, and how many numbers are above the average.




def list_analyser(numbers):
    smallest = float("inf")
    smallest_index = 0
    largest = float("-inf")
    largest_index = 0
    sum = 0
    above_avg_count = 0
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > largest:
            largest = list_of_numbers[i]
            largest_index = 1
        if list_of_numbers[i] < smallest:
            smallest = list_of_numbers[i]
            smallest_index = i
        sum += list_of_numbers[i]
    avg = sum / len(list_of_numbers)
    for number in list_of_numbers:
        if number > avg:
            above_avg_count += 1
    return (f"Smalles: {smallest} (at index {smallest_index})\nLargest: {largest} (at index {largest_index})\nTotal: {sum}\nAverage: {avg:.2f}\nNumbers above average: {above_avg_count}")

list_of_numbers = [12, 5, 27,8, 14, 27, 3]
print(list_analyser(list_of_numbers))