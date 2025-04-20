# Slicing
# Accept a string from user
s = input("Enter a string s: ")

# Slicing Operation

# First 4 chars from s - index 0 to 3
print(f"\nFirst 4 chars in {s} are {s[:4]}")

# Last 4 chars from s using # reverse indexing in negatives
print(f"\nLast 4 chars in {s} are {s[-4:]}") 

# Chars from index 2 to 5 from s
print(f"\nChars from index 2 to 5 in {s} are {s[2:6]}")