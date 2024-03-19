"""Presentation Layer."""
import os

import commands


class Option:
    """Pair the text to be displayed to the user 
    and the command it triggers
    """

    def __init__(self, name, command, prep_call=None) -> None:
        self.name = name  # The name displayed in th menu
        self.command = command  # instance of command to execute
        self.prep_call = prep_call  # preparation step to call before before executing command

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else \
            self.command.execute()
        print(message)

    def __str__(self) -> str:
        return self.name


def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print('Invalid choice')
        choice = input('Choose an option: ')
    return options[choice.upper()]


def get_user_input(label, required=True):
    """Prompt user for input. """
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():
    """Get necessary data for adding input."""
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False),
    }


def get_bookmark_id_for_deletion():
    """Get information for deleting bookmark."""
    return get_user_input('Enter a bookmark ID to delete')


def clear_screen():
    """Clear screen before printing the menu."""
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def loop():
    """Loop to perform several actions in a row."""
    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(),
                    prep_call=get_new_bookmark_data),
        'B': Option('List bookmarks by date',
                    commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title',
                    commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand(),
                    prep_call=get_bookmark_id_for_deletion),
        'Q': Option('Quit', commands.QuitCommand()),
    }
    clear_screen()
    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()
    _ = input("Press ENTER to return to menu")


if __name__ == "__main__":
    print("Welcome to Bark!")
    commands.CreateBookmarksTableCommand().execute()
    while True:
        loop()
