# check the number is armstrong number or not
# accept integer input from user
num = int(input("Enter int n: "))

# convert number to string to easy count of digits
num_str = str(num)

n = len(num_str)

# calculate sum of digits raised to power of n
a_sum = sum(int(digit)**n for digit in num_str)

# check if num is armstrong or not
if a_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")