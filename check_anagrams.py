# check anagrams
# Eg: Earth --> Heart, A gentleman --> Elegant man

# user defined function
def anagrams_check(str1, str2):
    # remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # compare sorted strings
    return sorted(str1) == sorted(str2)


# take input from user
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if anagrams_check(s1, s2):
    print("\nThe strings are anagrams.")
else:
    print("\nThe strings are not anagrams.")