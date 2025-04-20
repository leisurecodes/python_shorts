# Remove Punctuation from String
# import string package
import string

# remove punctuation function
def remv_punctuation(s):
    p = string.punctuation
    return ''.join(c for c in s if c not in p)

if __name__ == "__main__":
    s = "Hello!!!, Good to see you. " \
    "How are you?"

    new_s = remv_punctuation(s)

    print(f"\nOriginal String s: \n{s}")
    print(f"\nModified String new_s: \n{new_s}")

