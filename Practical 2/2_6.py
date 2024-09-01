def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Taking input from the user
score = float(input("Enter the student's score: "))
grade = determine_grade(score)
print(f"The student's grade is: {grade}")
