# count all words frequency of a sentence
# use remove_punctuations.py program as a module
import remove_punctuations as r

# function to count words freq
def words_freq(s):
    w = {} # empty dict
    # for loop
    for word in sorted(set(s.split())):
        c = s.count(word)
        w[word] = c
    return w

if __name__ == "__main__":
    s = 'Hi, How do you do? Good to see you.'

    print(f"\nOriginal String s: \n{s}")

    # remove punctuations
    new_s = r.remv_punctuation(s).lower()

    # call words_freq function
    result = words_freq(new_s)

    print("\nWords Frequency:")
    for words, count in result.items():
        print(f"{words} --> {count}")