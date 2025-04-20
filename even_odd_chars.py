# Accept string input from the user
user_string = input("Enter a string: ")

# Convert the string into a list and slice to get even and odd index characters
even_index_chars = list(user_string)[::2]
odd_index_chars = list(user_string)[1::2]

# Display the result
print(f"Chars at even index numbers: {even_index_chars}")
# print(even_index_chars)

print(f"Chars at odd index numbers: {odd_index_chars}")
# print(odd_index_chars)
