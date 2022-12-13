# Programmer: Kyle Kwan
# Date 10/24/2022
# File Name: Kwan-Calculator.py
# Description: This program is a calculator where you can choose one of the basic arithmetic operations and then input two numbers.
#              The code will calculate the answer from the two numbers and the user's choice of basic arithmetic operations.

# Defining functions.
def add(variable1, variable2):
    return variable1 + variable2

def subtract(variable1, variable2):
    return variable1 - variable2

def multiply(variable1, variable2):
    return variable1 * variable2

def divide(variable1, variable2):
    return variable1 / variable2

# User's decision of basic arithmetic operation to be used.
operation = input("Please select one option: Add/Subtract/Multiply/Divide: ")

print ("You chose", operation)

# Checks user's decision to see if it's valid.
if operation.lower() in ("add", "subtract", "multiply", "divide"):
    variable1 = float(input("Enter first number: "))
    variable2 = float(input("Enter second number: "))
    
    if operation.lower() == "add":
        print(variable1, "+", variable2, "=", add(variable1, variable2))

    elif operation.lower() == "subtract":
        print(variable1, "-", variable2, "=", subtract(variable1, variable2))

    elif operation.lower() == "multiply":
        print(variable1, "*", variable2, "=", multiply(variable1, variable2))

    elif operation.lower() == "divide":
        print(variable1, "/", variable2, "=", divide(variable1, variable2))
        
else:
    print("The option you chose (", operation, ") is not valid.\nPlease try this program again.")
    
# I'm not sure if this marks my grade but I use this to be able to keep the python shell window open.
input(f"\nPress enter to exit")