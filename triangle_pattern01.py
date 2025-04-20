# Right angle triangle pattern
# take input from user

rows = int(input("Enter no. of rows: "))

# loop to print
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == i:
            # last star without space
            print("*", end="")
        else:
            print("*", end=" ")
    # move to next line
    print()