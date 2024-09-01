#Write a program to solve a quadratic equation ax^2+bx+c=0.
import cmath

def solve_quadratic(a, b, c):
    d = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    return x1, x2

# Example usage:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
solutions = solve_quadratic(a, b, c)
print("The solutions are:", solutions)
