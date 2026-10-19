#Mathias-Nerd
#Monday exercise: week 6
#Question 3: Matrix Row Sums — With Column Sums and Row Averages
# Given a matrix (a list containing rows of numbers), calculate and display the total of each row, the total of each column, and the average of each row.
def matrix_sum(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        sum = 0
        if i == 0:
            column_total = row 
        for j in range(len(row)):
            sum += row[j]
            if i != 0:
                column_total[j] += row[j]
        avg = sum/ len(row)
        print(f"Row {i+1} total: {sum} | Row {i+1} average: {avg:.1f}")
    print()

    for k in range(len(column_total)):
        print(f"Column {k+1} total: {column_total[k]}")
    

matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
column_total = []
matrix_sum(matrix)

