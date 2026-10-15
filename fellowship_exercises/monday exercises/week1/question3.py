#Mathias Nerd
#Student grades

#Starting data
students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

for student in students:
    sum = round(student[1] + student[2] + student[3], 2)
    avg = round(sum / 3, 2)
    if avg <= 39:
        grade = 'F'
    elif avg <= 44:
        grade = 'E'
    elif avg <= 49:
        grade = 'D'
    elif avg <= 59:
        grade = 'C'
    elif avg <= 69:
        grade = 'B'
    else:
        grade = 'A' 
    print(f"{student[0]} - Average: {avg} - Grade: {grade}")
