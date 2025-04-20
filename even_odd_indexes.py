# Extract Characters in Even and Odd Indexes from a String
# Accept string input from the user
user_str = input("Enter a string: ")

# Characters in Even Indexes
print("Characters in Even Index")
for i in range(0, len(user_str), 2):
    print(f"index = {i}, char = {user_str[i]}")
print()

# Characters in Odd Indexes
print("Characters in Odd Index")
for i in range(1, len(user_str), 2):
    print(f"index = {i}, char = {user_str[i]}")
