#Write a program that takes the working hours and wages of 5 employees and calculates the salary of employees.
def calculate_salary(hours, wage):
    return hours * wage

# Example usage for 5 employees:
for i in range(1, 6):
    hours = float(input(f"Enter working hours for employee {i}: "))
    wage = float(input(f"Enter wage rate for employee {i}: "))
    salary = calculate_salary(hours, wage)
    print(f"Salary for employee {i} is: {salary}")
