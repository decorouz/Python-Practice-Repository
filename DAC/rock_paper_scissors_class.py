"""Class Implementation of Rock, Paper, Scissors."""
import random

OPTIONS = ["rock", "paper", "scissors"]


def print_options():
    """Display the available choices."""
    print("\n".join(f"({i+1}) {option.title()}" for i, option in enumerate(OPTIONS)))


class RockPaperScissorsSimulator:
    """Rock, Paper and Scissors game."""

    def __init__(self) -> None:
        self.human_choice = None
        self.computer_choice = None

    def get_computer_choice(self):
        """Get human choice."""
        self.computer_choice = random.choice(OPTIONS)

    def get_human_choice(self):
        """Get human choice."""
        user_input = self.human_choice = int(input("Inter the number of choice: "))
        self.human_choice = OPTIONS[user_input - 1]

    def print_choices(self) -> None:
        """Display human and computer choices.

        Parameters
        ----------
        human_choice
            Human choice
        computer_choice
            Computer choice
        """
        print(f"You chose {self.human_choice}")
        print(f"The computer choose {self.computer_choice}")

    def print_win_lose(self, human_beats, human_loses_to):
        """Print win or lose outcome."""
        if self.computer_choice == human_loses_to:
            print(f"Sorry, {self.computer_choice} beats {self.human_choice}")
        elif self.computer_choice == human_beats:
            print(f"Yes, {self.human_choice} beats {self.computer_choice}!")

    def print_result(self):
        """Print result."""
        if self.human_choice == self.computer_choice:
            print("Draw")
        if self.human_choice == "rock":
            self.print_win_lose("scissors", "paper")
        elif self.human_choice == "paper":
            self.print_win_lose("rock", "scissors")
        elif self.human_choice == "scissors":
            self.print_win_lose("paper", "rock")

    def simulate(self):
        """Stimulate the game."""
        while True:
            print_options()
            self.get_human_choice()
            self.get_computer_choice()
            self.print_choices()
            self.print_result()
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                print("Game over")
                break


RPS = RockPaperScissorsSimulator()
RPS.simulate()
