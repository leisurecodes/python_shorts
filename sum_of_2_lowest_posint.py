# Create a function that returns the 
# sum of the two lowest positive numbers 
# given an array of minimum 4 positive integers. 
# No floats or non +ve integers will be passed.

# For example, when an array is passed like 
# 
# [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] return 3453455.

#--------------CODE HERE-----------------------------------

# take list from user

l = list(map(int, input("Enter list items: ").split(", ")))

new_l = sorted(l)

s = new_l[0] + new_l[1]

print(f"{l} --> {s}")