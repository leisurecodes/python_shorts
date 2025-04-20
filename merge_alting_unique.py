# Merge two lists into one list 
# alernating the values avoid duplicates

# function to merge lists
def merge_alt_unique(list1, list2):
    merged = []
    seen = set()
    i = 0
    while i < len(list1) or i < len(list2):
        for lst in (list1, list2):
            if i < len(lst) and lst[i] not in seen:
                merged.append(lst[i])
                seen.add(lst[i])
        i += 1
    return merged



# take input from user
l1 = [4, 5, 6]

l2 = [1, 2, 3, 4, 5, 6]

print(merge_alt_unique(l1, l2))
