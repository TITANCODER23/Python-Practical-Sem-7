def self_division():
    while True:
        try:
            number1 = int(input("Enter the First number: "))
            number2 = int(input("Enter the Second number: "))
            
            result = float(number1 / number2)
            
            print(f" {number1} / {number2} is {result}")
            break
        
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except Exception as e:
            print("An error occurred:", e)
       

self_division()