# Display Pyramid Pattern
# take no. of rows from the user
rows = int(input("Enter no. of rows: "))

# loop through each row
for i in range(1, rows + 1):
    # print spaces before stars for centering
    print("  " * (rows - i), end = "")

    # print stars with space
    # (2*i -1 stars in each row)
    for j in range(1, 2 * i):
        if j == 2 * i - 1:
            # no space afte the last star
            print("*", end = "")
        else:
            print("*", end = " ")
    
    print() # move to next line