# find all prime nums in a  range
# take start and end of range from user
s, e = map(int, input("start, end: ").split())

print(f"\nPrime numbers b/w {s} and {e} are:")

for num in range(s, e + 1):
    if num > 1:  # all primes are > 1
        for i in range(2, num - 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()