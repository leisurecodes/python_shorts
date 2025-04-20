# Display Fibonacci Series up to n terms
# accept integer input from user

n = int(input("Enter number of terms n: "))

# declare a and b
a, b = 0, 1

print("Fibonacci Series: ")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
