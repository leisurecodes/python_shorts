# count vowels and consonants in a string
# initialize
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

v = 0  # Vowels count
c = 0  # Consonants count

# take input from user
s = input("\nEnter a string s: ")

print(f"String s: {s}")

# loop to iterate over string
for i in s:
    # lower() converts uppercase to lowercase
    if i.lower() in vowels:
        v += 1
    elif i.lower() in consonants:
        c += 1

print(f"No. of Vowels: {v}")
print(f"No. of Consonants: {c}")