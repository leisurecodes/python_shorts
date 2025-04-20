# check whether number is numeric palindrome
# take input from the user

num = int(input("Enter a number: "))

# reverse the number using string reverse operation
r_num = int(str(num)[::-1])

# check if num & r_num are the same or not
if num == r_num:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")