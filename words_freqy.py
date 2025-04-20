# Count all words frequecy of a sentence

import string

s = 'Hi, How do you do? Good to see you.'

print(f"\nOriginal String s: \n{s}")

# Remove Punctuations from Strig
p = string.punctuation
new_s = "".join(i for i in s if i not in p)

print(f"\nModified String new_s: \n{new_s}")

# ============================================

# Count words frequency
new_s = new_s.lower()

# for loop
print("\nWords Frequency:")
for word in sorted(set(new_s.split())):
    c = new_s.count(word)
    print(f"{word} --> {c}")

