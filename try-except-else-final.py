try:
    # code that can give error goes here
    num = int(input("Enter integer num: "))
    result = 10 / num

except ZeroDivisionError:
    # runs if num is zero (division by zero)
    print("Can't divide by zero!")

except ValueError:
    # runs if the input is not an integer
    print("Invalid input! Enter valid number.")

else:
    # runs if try block runs without exceptions
    print(f"Success! The result is: {result}")

finally:
    # always runs
    print("Execution complete. Thank you!")
