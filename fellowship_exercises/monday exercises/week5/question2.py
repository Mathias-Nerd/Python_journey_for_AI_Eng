#Mathias-Nerd
#Week 4: Question 2
#Given a list and a target value, search through the list one item at a time. Print the index where the target first appears, or a message saying it was not found.

values = [14, 7, 22, 9, 7, 31]
# values = [25, 2, 3, 5, 3, 23]
target = 7
i = 0
found = False
while not found and i < len(values):
    if target == values[i]:
        print(f"Found at index {i}")
        found = True
    i += 1
if not found:
    print("Target not found")
