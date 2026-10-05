#Mathias-Nerd
#Fellowship exercise 
#Week3: Question 3: Studdnt grades

students = [{"name": "Sam", "scores": [80, 90]},{"name": "David", "scores": [55, 60]}]

highest = 0
highest_name = ""
lowest = 101
lowest_name = ""

for student in students:
    sum = 0
    for score in student["scores"]:
        sum += score
    avg = sum / len(student["scores"])
    
    if avg >= 70:
        grade = "A"
    elif avg >=60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 45:
        grade = "D"
    elif avg >= 40:
        grade = "E"
    else:
        grade = "F"
        
    print(f"{student["name"]} → Average: {avg:.2f} → Grade: {grade}")
    
    if avg > highest:
        highest = avg
        highest_name = student["name"]
    if avg < lowest:
        lowest = avg
        lowest_name = student["name"]
    
print(f"Highest performing student is {highest_name} with the score {highest:.2f}")
print(f"Lowest performing student is {lowest_name} with the score {lowest:.2f}")