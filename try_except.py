def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except ValueError:
        print("Error: Invalid input! Please enter valid numbers.")

divide_numbers()