#Write a program to check if the input year is a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = int(input("Enter a year: "))
print("Is leap year:", is_leap_year(year))
