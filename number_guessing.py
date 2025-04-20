# number guessing game
# import random package
import random

# generate a random number between 1 & 100
secret_number = random.randint(1, 100)

print("Number Guessing Game!")
print("Think of a number between 1 and 100")

attempt = 1

# Infinite loop until user guess correctly
while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Guessed in {attempt} attempts.")
        break
    attempt += 1