"""A simple guessing game to demonstrate the use of `else` inside while loop
A player has to guess a number between the range of 1 and n."""

from random import randint

# Initialize the the game
GUESS = 0

# Initialize the guess range
UPPER_BOUND = 50
LOWER_BOUND = 1

# Set the secret random number(int) to be guess
to_be_guessed = randint(LOWER_BOUND, UPPER_BOUND)
print(to_be_guessed)

while GUESS != to_be_guessed:
    GUESS = int(input("Num number: "))
    if GUESS == 0:
        print("Sorry that you are giving up")
        break
    if GUESS < LOWER_BOUND or GUESS > UPPER_BOUND:
        print("Your guess is out of range")
    elif GUESS > to_be_guessed:
        UPPER_BOUND = GUESS - 1
        print("Guess Number too large")
    elif GUESS < to_be_guessed:
        LOWER_BOUND = GUESS + 1
        print("Guessed Number is too small")
else:
    print("Congratulation, you made it here")
