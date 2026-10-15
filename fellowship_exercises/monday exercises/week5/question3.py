#Mathias-Nerd
#Week 4: Question 3
#Given a matrix (a list containing rows of numbers), calculate and display the total of each row.
# Use this starting matrix: matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 3
matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
for row in matrix:
    total = 0
    for i in range(len(row)):
        total += row[i]
    print(f"Row {i + 1} total: {total}")
