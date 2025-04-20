# Try-Except-Else-Finally Blocks
try:
    # Try block: Code that might raise an error
    n = int(input("Enter number n: "))
    result = 10 / n
    print(f"\nResult is: {result}")

except ValueError as v:
    # This runs if input is not a number
    print(f"\n{v}: \nEnter a valid number.")

except ZeroDivisionError as z:
    # This runs if the number is zero
    print(f"\n{z}: \nCan't divide by zero.")

except:
    # This deals any unexpected Errors
    print("\nThis block catch any error. " \
          "Used to deal with unexpected errors.")
    
finally:
    # This block always runs, no matter what
    print("\nThis is the 'finally' block. " \
          "It always executes.")
