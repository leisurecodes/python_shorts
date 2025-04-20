# reverse a number
# take integer input from user
num = int(input("Enter a number: "))
# r_num = 0

# while num > 0:
#     digit = num % 10           # get last digit
#     r_num = r_num * 10 + digit
#     num //= 10                 # remove last digit

# print(f"Reversed number is {r_num}")


# Reverse the number using string slicing
r_num = int(str(num)[::-1])

print(f"Reversed number is {r_num}")
