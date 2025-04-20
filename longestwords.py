# Find all longest words in the sentence
# user defined function
def longest_words(s):
    words = s.split()
    max_len = max(len(w) for w in words)
    l = [w for w in words if len(w) == max_len]
    return l


s1 = "Python is really fun to learn"
print(f"\ns1: {s1}")
print(f"From s1: {longest_words(s1)}")

s2 = "Elephant reaching for mango from branches"
print(f"\ns2: {s2}")
print(f"From s2: {longest_words(s2)}")
