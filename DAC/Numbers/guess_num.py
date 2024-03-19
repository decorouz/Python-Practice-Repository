import random


def guessing_game():

    # Welcome player to the game
    name = input("\nPlease enter your name to begin\n")
    print(f"Welcome {name}!\n\n Guess a number between 1-100\n")
    target_number = random.randint(10, 100)
    attempts = 3

    while attempts > 0:
        print(f"\n Total attempts left: {attempts}")

        # Track a valid guess attempt
        correct_attempt = False

        try:
            # Check a valid guess
            answer = int(input("Please guess a number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if answer == target_number:
            print(f"Right! The answer is {answer}")
            break

        if answer < target_number:
            print(f"Your guess of {answer} is too low ")
            correct_attempt = True

        else:
            print(f"Your guess of {answer} is too high!")
            correct_attempt = True

        if correct_attempt:
            attempts -= 1

    print(f" Sorry you lost! The target number is {target_number}")


guessing_game()
