# Given a randon non-integer number,
# return the digits of this number
# within an list in reverse order

# 34681 ==> [1,8, 6, 4, 3]
# 0     ==> [0]

# =================Code Here=================


# take int input from user
n = int(input("Enter integer n: "))

l = []  # empty list

for i in str(n)[::-1]:
    l.append(int(i))

print(f"\n {n} ==> {l}")
