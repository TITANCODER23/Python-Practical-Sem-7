#Write a program to calculate the grade based on the percentage score.

def calculate_grade(score):
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

# Example usage:
percentage = float(input("Enter the percentage score: "))
grade = calculate_grade(percentage)
print("Your grade is:", grade)
