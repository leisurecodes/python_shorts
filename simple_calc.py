# Simple Calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Can't divide by zero"
def exponent(n1, n2):
    return n1 ** n2

# take input from user
op = input("Enter operator +, -, *, /, **: ")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

# if else statements
if op == "+":
    print(add(num1, num2))
elif op == "-":
    print(subtract(num1, num2))
elif op == "*":
    print(multiply(num1, num2))
elif op == "/":
    print(divide(num1, num2))
elif op == "**":
    print(exponent(num1, num2))
else:
    print("Invalid Option!")