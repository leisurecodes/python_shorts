# swap first and last characters of a string

# take input from user
s = input("\nEnter a string: ")

# swap
new_s = s[-1] + s[1 : -1] + s[0]

print(f"\n{s} --> {new_s}")
