# Find frequency of characters in a string

# take input from user
string = input("Enter a string: ")
s = string.lower()  # convert to lowercase


# for loop
for i in sorted(set(s)):
    c = s.count(i)  # gives the count of occurrences
    print(f"{i} --> {c}")
    