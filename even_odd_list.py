# program to separate even and odd from list
l = list(range(10, 23)) # gives list 10 to 22

print("\nOriginal List: ")
print(l)

# separate even and odd
even = [] # empty lists
odd = []

for i in l:
    odd.append(i) if i % 2 else even.append(i)

# print both lists
print(f"\nEven List: {even}")
print(f"Odd List: {odd}")