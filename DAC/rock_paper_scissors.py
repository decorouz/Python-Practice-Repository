"""Rock, Paper, Scissor Implementation."""
import random

OPTIONS = ["rock", "paper", "scissors"]


def get_computer_choice():
    """Get computer choice."""
    return random.choice(OPTIONS)


def get_human_choice():
    """Get human choice."""

    user_input = int(input("Enter the number[1-3] of your choice: "))
    return OPTIONS[user_input - 1]


def print_options():
    """Display the avialable choices."""
    print(
        "\n".join(
            f"({i+1}) {option.title()}" for i, option in enumerate(OPTIONS)
        )
    )


def print_choices(human_choice: str, computer_choice: str) -> None:
    """Display human and computer choices.

    Parameters
    ----------
    human_choice
        Human choice
    computer_choice
        Computer choice
    """
    print(f"You chose {human_choice}")
    print(f"The computer choose {computer_choice}")


def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    """Print win or lose outcome."""
    if computer_choice == human_loses_to:
        print(f"Sorry, {computer_choice} beats {human_choice}")
    elif computer_choice == human_beats:
        print(f"Yes, {human_choice} beats {computer_choice}!")


def print_result(human_choice, computer_choice):
    """Print result."""
    if human_choice == computer_choice:
        print("Draw")
    if human_choice == "rock":
        print_win_lose("rock", computer_choice, "scissors", "paper")
    elif human_choice == "paper":
        print_win_lose("paper", computer_choice, "rock", "scissors")
    elif human_choice == "scissors":
        print_win_lose("scissors", computer_choice, "paper", "rock")


if __name__ == "__main__":
    while True:

        print_options()
        h_choice = get_human_choice()
        c_choice = get_computer_choice()
        print_choices(h_choice, c_choice)
        print_result(h_choice, c_choice)
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print("Game over")
            break
