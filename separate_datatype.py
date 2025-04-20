# separate datatypes in list

mixed_list = [10, "Ram", 23, 1.5, True, "False"]

# Take input from user as a comma-separated string
# user_input = input("Enter elements separated by commas (e.g. 1, 'hello', 3.5, True): ")

# Convert input into a list using eval (⚠️ Use with caution — see note below)
# mixed_list = eval(f"[{user_input}]")

# Create empty lists for each type
integers = []
floats = []
strings = []
booleans = []
others = []

# Separate based on type
for item in mixed_list:
    if isinstance(item, bool):
        booleans.append(item)
    elif isinstance(item, int):
        integers.append(item)
    elif isinstance(item, float):
        floats.append(item)
    elif isinstance(item, str):
        strings.append(item)
    else:
        others.append(item)

# Print results
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", booleans)
print("Others:", others)

