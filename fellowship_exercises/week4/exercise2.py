#Mathias-Nerd
#Question 2: Student grades

students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 30]}
]

def grade_for(avg):
    if avg > 70:
        return "A"
    elif avg > 60:
        return "B"
    elif avg > 50:
        return "C"
    elif avg > 45:
        return "D"
    elif avg > 40:
        return "E"
    else:
        return "F"

# lowest_no = float("inf")
# lowest_name = ""
# highest_no = float("-inf")
# highest_name = ""

def compute(dict):
    res = []
    name = dict["name"]
    sum = 0
    for score in dict["scores"]:
        sum += score
    avg = sum / len(dict["scores"])
    grade = grade_for(avg)
    res.append(name)
    res.append(avg)
    res.append(grade)

    return tuple(res)
    # global highest_no
    # if avg > highest_no:
    #     highest_no = 
averages = map(compute, students)
result = list(averages)
grade = [x[2] for x in result]
# print(scores)
print(result)

def passed(student):
    grade = student[2]
    if grade in ['A', 'B', 'C']:
        return True
    else:
        return False

passes = list(filter(passed, result))
people_that_passed = [x[0] for x in passes]
print(f"People that passed {people_that_passed}")