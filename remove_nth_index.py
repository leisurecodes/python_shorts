# remove nth index from a string
# remove character from a string by index

# take input from user
s = input("Enter a string: ")

n = int(input("Enter a index number: "))

if n < len(s):
    new_s = s[:n] + s[n+1:]
    print(new_s)

else:
    print(f"Index {n} is out of range.")