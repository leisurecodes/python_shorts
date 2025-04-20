# try except else finally blocks
try:
    # code that can give error goes here
    num = int(input("Enter integer num: "))
    r = 10 / num

except ZeroDivisionError:
    # runs if num is zero - division by zero
    print("Can't divide by zero.")

except ValueError:
    # runs if the input is not an integer
    print("Invaid input! Enter valid num.")

except Exception as e:
    # deals with any unexpected error
    print(f"Caught unexpected error: {e}")

else:
    # runs if try bloc runs without exceptions
    print(f"Success! Result: {r}")

finally:
    # always runs
    print("Execution Complete. Thanks!")
