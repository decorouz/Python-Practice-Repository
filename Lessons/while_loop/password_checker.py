"""Demonstrating the use of else within a while loop."""

CORRECT_PASSWORD = "password"
MAX_ATTEMPT = 3
ATTEMPT = 0

while ATTEMPT < MAX_ATTEMPT:
    input_pass = input("Enter the password: ")
    if input_pass == CORRECT_PASSWORD:
        print("Success! You have entered the current password!")
        break
    ATTEMPT += 1
    REMAINING_ATTEMPTS = MAX_ATTEMPT - ATTEMPT
    if REMAINING_ATTEMPTS > 0:
        print(f"Incorrect password. You have {REMAINING_ATTEMPTS} attempt left")
    else:
        print("Maximum attemp exceeded. You are locked out")
