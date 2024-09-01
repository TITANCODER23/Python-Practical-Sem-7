#WAP to convert days into months and days:
total_days = int(input("Enter the number of days: "))
months = total_days // 30
days = total_days % 30
print(f"{total_days} days is equivalent to {months} months and {days} days.")
