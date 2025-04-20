# find index of the element given

def find_ele_index(l, target):
    for i, row in enumerate(l):
        for j, value in enumerate(row):
            if value == target:
                # return row and col index
                return (i, j)
    return None # if element not found

# list
l = [
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
]

# find element
t = int(input("Enter number to find: "))
r = find_ele_index(l, t)

if r:
    print(f"{t} is found at index ({r[0]}, {r[1]})")
else:
    print(f"{t} not found.")