import random
import string

def generate_password(min_len = 7, max_len = 11):
    # char sets
    uc_letters = string.ascii_uppercase
    lc_letters = string.ascii_lowercase
    dgts = string.digits
    sp_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # password len
    pwd_len = random.randint(
        min_len, max_len
    )

    # atleast one char from each category in pwd
    password = [
        random.choice(uc_letters),
        random.choice(lc_letters),
        random.choice(dgts),
        random.choice(sp_chars)
    ]

    # fill remaining len with random chars
    # from all categories
    all_chars = uc_letters+lc_letters+dgts+sp_chars
    password.extend(
        random.choice(
            all_chars
        ) for _ in range(
            pwd_len - 4
        )
    )

    # shuffle password chars
    random.shuffle(password)

    # convert pssword list to string
    return ''.join(password)

if __name__ == "__main__":
    password = generate_password()
    print(f"Generated password: \n{password}")