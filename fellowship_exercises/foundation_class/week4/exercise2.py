#Given a list of dictionaries representing students and their scores, calculate each student's average and assign a letter grade.

def calc_avg(scores: list[int]) -> float:
    sum = 0
    for score in scores:
        sum += score
    return float(f"{sum / len(scores):.2f}")


def grade_for(avg: float) -> str:
    grade = ""
    if avg >= 70:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    elif grade >= "40":
        grade = "E"
    else:
        grade = "F"

    return grade


#This function does the computation for one student
#We will use map to run this function for all students
def compute(student: dict) -> tuple :
    name, score = student.values()
    avg = calc_avg(score)
    grade = grade_for(avg)
    
    return name, avg, grade

def passed(result):
    """Returns True is student's grade is either A, B, or C otherwise False
    """
    passed_grades = ["A", "B", "C"]
    if result[2] in passed_grades:
        return True

    return False

def get_highest_and_lowest(results):
    lowest = float("inf")
    lowest_name = ""
    highest = float("-inf") 
    highest_name = ""
    for result in results:
        if result[1] > highest:
            highest = result[1]
            highest_name = result[0]

        if result[1] < lowest:
            lowest = result[1]
            lowest_name = result[0]

    return f"The highest scoring student is {highest_name} with the score of {highest}\nThe lowest scoring student is {lowest_name} with the score of {lowest}"




students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},
    {"name": "Mike", "scores": [25, 30]},
    {"name": "Kyle", "scores": [50, 70]}
]

#Map to produce list of (name, avg, grade) tuples
students_result = list(map(compute, students))

print(students_result)

#Filter to produce a list of students who passed

students_that_passed = filter(passed, students_result)
print(f"Students that passed: {list(students_that_passed)}")


print(get_highest_and_lowest(students_result))
