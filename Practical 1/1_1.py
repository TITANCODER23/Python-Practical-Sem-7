 #Program (WAP) to calculate area and perimeter of a square:
 
def calculate_square_properties(side_length):
     if side_length <= 0:
         return "Invalid input: side length must be a positive number."

     area = side_length ** 2
     perimeter = 4 * side_length

     return area, perimeter
 
 # Test the function with side length 5

area, perimeter = calculate_square_properties(5)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")