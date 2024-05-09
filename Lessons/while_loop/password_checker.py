"""Demonstrating the use of else within a while loop."""

# ? Write a Python program that simulates a simple password checker.
# ?The program should ask the user to enter a password and continue to prompt them until
# ?they enter the correct password. Once the correct password is entered, the program should print a success message.

CORRECT_PASSWORD = "password"
MAX_ATTEMPT = 3
ATTEMPT = 0

while ATTEMPT < MAX_ATTEMPT:
    user_input = str(input("Enter your password: "))
    if user_input == CORRECT_PASSWORD:
        print("Success: You've enter the correc password")
        break

    else:
        ATTEMPT += 1
        remaining_attempt = MAX_ATTEMPT - ATTEMPT
        if remaining_attempt > 0:
            print(f"Incorrect Password! You have {remaining_attempt} attempt(s) left")
        else:
            print("Maximum attempts exceeded, you are now locked out!")
