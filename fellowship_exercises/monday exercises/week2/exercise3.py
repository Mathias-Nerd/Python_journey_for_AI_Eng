#Fellowship exercise
#Week 2
#Student grades

students = [["Samuel", 80, 75, 90], ["David", 55, 60, 50], ["Mary", 35, 40, 30], ["John", 65, 70, 68],["Janet", 90,80,70]]


def calculate_grade(avg):
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
    return grade

for student in students:
    sum = 0
    for i in range(1, len(student)):
        sum = sum + student[i]
    avg = sum / (len(student) - 1)   
    grade = calculate_grade(avg)    
    print(f"{student[0]} → Average: {round(avg, 2)} → Grade: {grade}")