# Ask the user for two numbers and an operation
num1 = float(input("Enter the first number: "))  #Ask user to enter the first number
num2 = float(input("Enter the second number: ")) #Ask user to enter the second number
operation = input("Enter the operation (+, -, *, /): ") #Ask user to choose an operation

# Perform the operation
if operation == "+":
    result = num1 + num2  #Perform addition
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2  #Perform subtraction
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2  #Perform multiplication
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
#check if the second number is zero 
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
