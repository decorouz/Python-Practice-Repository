"""Prime number checker"""


def prime(num: int) -> bool:
    """Check if a given number is prime"""
    if num <= 1:
        return False
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a positive integer: "))

# Initialize a variable to keep track of the divisors
DIVISOR = 1

# Initialize a variable to determine if the number is prime
IS_PRIME = True

# Use a while loop to check for DIVISORs
while DIVISOR <= number // 2:
    DIVISOR += 1
    if number % DIVISOR == 0 and IS_PRIME:
        IS_PRIME = False
        break  # If a DIVISOR is found, exit the loop


# Display the result
if IS_PRIME:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
