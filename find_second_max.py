# Find the second rank or second max from the
# list of percentages

# get percentages list from user
print("Enter list of percentages: ")
scores = list(map(int, input().split()))

# remove duplicates
unique_scores = list(set(scores))

# sort in descending order
unique_scores.sort(reverse=True)

print(f"\nList of Scores: {scores}")

# print second highest or second max
print(f"Second Rank %ge: {unique_scores[1]}")

