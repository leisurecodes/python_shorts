# remvoe duplicate chars from a string
# take input from user
s = input("Enter a string s: ")

# display original string
print(f"\nString s: {s}")

# take a new variable
new_s = ""  # empty

# removing duplicate characters
for i in s.lower():
    # lower() converts uppercase to lowercase
    if i in new_s:
        pass
    else:
        new_s += i

print(f"After removing duplicates: {new_s}")