# Find factorial of a number using recursive function

# recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# accept integer input from user
num = int(input("Enter num: "))

if num < 0:
    print("Factorial is not defined for -ve nums")
else:
    result = factorial(num)
    print(f"Factorial of {num} is {result}")