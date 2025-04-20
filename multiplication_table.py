# Multiplication table of a integer number
# take integer input from the user
n = int(input("Enter a integer n: "))

# Display the table from 1 to 10
print(f"\nMultiplication table of {n}:")

for i in range(1 ,11):
    print(f"{n} x {i} = {n * i}")