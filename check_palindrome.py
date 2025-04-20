# check a string is palindrom
# accept a string from user
s = input("Enter a string: ")

# check palindrome
# note: s[::-1] is reverse of s
if s == s[::-1]:
    print(f"{s} is Palindrome")
else:
    print(f"{s} is not Palindrome")