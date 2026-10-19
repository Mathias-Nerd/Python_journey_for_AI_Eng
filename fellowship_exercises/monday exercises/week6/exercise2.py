#Mathias-Nerd
#MOnday exercise: week 6
#Question 2:  Linear Search — All Occurrences + Count
#Given a list and a target value, find every index where the target appears. Print all matching indices, the total count of matches, and the index of the first and last occurrence. If the target does not appear, print a not-found message.
def linear_search(numbers, target):
    result = []
    for i in range(len(values)):
        if values[i] == target:
            result.append(i)
    if not result:
        print("Target not found")
    else:
        first = result[0]
        last = result[-1]
        print(f"Found at indices: {result} | Count: {len(result)} | First {first} | Last: {last}")

values = [14, 7, 22, 9, 7, 31, 7, 5]
target = 7


linear_search(values, target)