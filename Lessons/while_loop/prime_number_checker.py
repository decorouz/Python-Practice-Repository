"""Prime Number Checker"""

# ? Write a Python program that checks whether a given positive integer is a prime number.
# ? The program should ask the user to input a number and then use a while loop to determine if the number is prime.
# Prime number: Number divisible by its and 1


number = int(input("Enter a positive integer: "))

# Initialize a variable to keep track of the divisors
DIVISOR = 2

# Initialize a variable to determine if the number is prime
IS_PRIME = True

# Use a while loop to check for DIVISORs
if number < 2:
    IS_PRIME = False
else:

    while DIVISOR <= number**0.5:
        if number % DIVISOR == 0 and IS_PRIME:
            IS_PRIME = False
            break  # If a DIVISOR is found, exit the loop
        DIVISOR += 1

# Display the result
if IS_PRIME:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
