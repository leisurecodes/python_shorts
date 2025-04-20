# find LCM and GCD (HCF) of two numbers
# using math library

import math

# take input from the user
a, b = map(int, input("Enter a b: ").split())

# calculate GCD using math.gcd
gcd = math.gcd(a, b)

# calculate LCM using math.lcm
lcm = math.lcm(a, b)

# print results
print(f"\nGCD of {a} and {b} is {gcd}")
print(f"LCM of {a} and {b} is {lcm}")