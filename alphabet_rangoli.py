# Alphabet Rangoli - HackerRank Challenge

# for size s 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

import string

def display_rangoli(s):
    a = string.ascii_lowercase
    w = 4 * s - 3

    rows = [
        '-'.join(
            a[s-1 : i: -1] + a[i : s]
        ).center(w, '-') for i in range(s)
    ]

    # combine top and bottom halves
    print("\n".join(rows[::-1] + rows[1:]))

n = int(input("Enter size  (1 to 26): "))
display_rangoli(n)
