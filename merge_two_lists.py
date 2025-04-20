# Merge two variable length lists into one list
# avoid duplicates

def merge_lists(l1, l2):
    merged = []
    for i in l1 + l2:
        if i not in merged:
            merged.append(i)
    return merged

a = [1, 2, 3, 4]
b = [3, 4, 5, 6, 7, 8]

# merge
result = merge_lists(a, b)
print(f"\na : {a}")
print(f"\nb : {b}")
print(f"\nMerged List : {result}")