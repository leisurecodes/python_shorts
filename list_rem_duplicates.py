# Remove duplicates in a list

l = ["Hi", 1, 2, 2, 3, 3, "Hi"]

# empty list
new_l = []

# for loop
for i in l:
    if i not in new_l:
        new_l.append(i)

# print
print("\nUsing for loop - Order preserved")

print(f"{l} --> {new_l}")

# Using set() to remove duplicates
print("\nUsing sets - Unordered")

new_l = set(l)

# set is unordered, no order at output
print(f"{l} --> {new_l}")
