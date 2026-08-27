"""
Write a function analyse_students(threshold, **student_scores) that calculates the average score for each student, filters out anyone who falls below the threshold, and returns a formatted summary of qualifying students.
threshold is a number representing the minimum passing average (e.g., 70).
**student_scores collects student names as keys and a tuple of their numerical test scores as values (e.g., Alice=(85, 90, 92)).
Calculate the average test score for each student.
Keep only students whose average score is greater than or equal to threshold.
Sort qualifying students in descending order by their average score.
Return a single formatted string structured like this:
"1. Alice - Avg: 89.0 | 2. Charlie - Avg: 75.0"
"""


def analyse_students(threshold, **student_scores):
    # Calclating the averages
    calculated_list = [(name, sum(values)/len(values))
                       for (name, values) in student_scores.items()]

    # Filtering
    filtered_list = [(name, avg)
                     for name, avg in calculated_list if avg >= threshold]

    #   Sorted list
    sorted_list = sorted(filtered_list, key=lambda x: x[1], reverse=True)

    # Output string
    output_list = [f"{i + 1}. {name} - Avg: {avg}" for i,
                   (name, avg) in enumerate(sorted_list)]

    output_string = " | ".join(output_list)
    return output_string


result = analyse_students(
    70, Alice=(85, 90, 92), Bob=(60, 70, 65), Charlie=(75, 80, 70)
)
print(result)
