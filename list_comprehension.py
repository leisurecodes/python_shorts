# Condition: i + j + k != n
# x, y, z = 1, 1, 2
# n = 3
#Output: [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], 
#           [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

x, y, z = map(
    int,
    input("Enter x, y, z: ").split(", ")
)
n = int(input("Enter n: "))

result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]

print(result)

