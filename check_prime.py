# check prime number or not
# integer input from user

n = int(input("Enter a integer number n: "))

# Prime number check
if n <= 1:
    print(f"{n} is not a prime number.")
else:
    for i in range(2, n-1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")