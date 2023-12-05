"""A simple guessing game to demonstrate the use of else inside while loop"""
from random import randint

GUESS = 0
UPPER_BOUND = 50
LOWER_BOUND = 1
to_be_guessed = randint(LOWER_BOUND, UPPER_BOUND)
print(to_be_guessed)

while GUESS != to_be_guessed:
    GUESS = int(input("New number : "))
    if GUESS == 0:
        print("Sorry you are giving up")
        break
    if GUESS < LOWER_BOUND or GUESS > UPPER_BOUND:
        print("Guess not within boundaries")
    elif GUESS > to_be_guessed:
        UPPER_BOUND = GUESS - 1
        print("Number too high")
    elif GUESS < to_be_guessed:
        LOWER_BOUND = GUESS + 1
        print("Number is too small")
else:
    print("Congratulations, you made it here")
