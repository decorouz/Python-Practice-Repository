import random

# I used underscore for variables and functions to indicate they are private

_WORD_LIST = [
    "python", "c", "java", "swift", "html", "css", "go", "ruby", "javascript"
]

_max_failed_attempts = 9


def _pick_random_word():
    return random.choice(_WORD_LIST)


def _make_word_classified(word):
    return ["_"] * len(word)


def _play_again():
    try_again = input("You want to play again (write y or n)>: ")

    if try_again == "y":
        play_guessing_game()
    else:
        print("\n Goodbye! \n")


def play_guessing_game():
    """A functions to choose a random word from a list of words 
    and then ask user to guess the one character at time"""

    name = input("\nTo play, enter your first name>: ")
    print(
        f"\n\t\t\t Welcome {name}! \n\n\n\t\t ***Word Guessing Game*** \n\n")

    target_word = _pick_random_word()
    classified_word = _make_word_classified(target_word)

    # count how many attempts are left
    attempts_left = _max_failed_attempts

    # list to track wrong guessed characters
    wrong_list = []

    while attempts_left > 0:
        print(*classified_word,
              f"\n\nTotal attempts left: {attempts_left}\n\n")

        answer = input("Guess a letter(Write only one letter)>: ").lower()

        if len(answer) != 1:
            print("Exactly one letter is expected!")
            continue

        if not answer.isalpha():
            print("A valid letter is required!")
            continue

        if answer in wrong_list:
            print("You have already guessed this letter")
            continue

        attempt_correct = False

        # check if the guessed answer matches the original word
        if answer in target_word:
            for char_idx, target_char in enumerate(target_word):
                if answer == target_char:
                    classified_word[char_idx] = answer
                    attempt_correct = True
        else:
            print("Your guess is wrong\n")
            wrong_list.append(answer)

        if not attempt_correct:
            attempts_left -= 1

        if "_" not in classified_word:
            """check whether it still contains an underscore to check if we're done."""
            print("\nYAY: You have guessed the letter correctly. \nYou won!\n")
            _play_again()
            return

    print("\nSorry you lost\n")

    # Prompt the user play again
    _play_again()


if __name__ == "__main__":
    play_guessing_game()
