# Take input from the user
num = int(input("Enter a number: "))

# Reverse the number with while loop
# n = num
# r_num = 0

# while n > 0:
#     digit = n % 10    # get last digit
#     r_num = r_num * 10 + digit
#     n //= 10          # remove last digit

# Reverse the number using string method
r_num = int(str(num)[::-1])

# Check if the num & r_num are the same
if num == r_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
