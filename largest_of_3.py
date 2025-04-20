# Find largest of three numbers
# take numbers from user

n1 = int(input("Enter number n1: "))
n2 = int(input("Enter number n2: "))
n3 = int(input("Enter number n3: "))

# Compare numbers
if n1 >= n2 and n1 >= n3:
    largest = n1
elif n2 >= n1 and n2 >= n3:
    largest = n2
else:
    largest = n3

print(f"\nThe largest number is {largest}")