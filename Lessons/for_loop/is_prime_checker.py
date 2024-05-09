"""Write a program to find and print all prime numbers between 1 and 50 using a for loop."""


def print_prime_numbers(limit: int):
    """Print prime numbers within specified limit"""

    print(f"Prime numbers between 1 and {limit}:")
    for number in range(1, limit + 1):
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
            # print(number)
            print(number, end=", ")


# * Another Approach to solving the problem
def print_prime_numbers1(limit: int):
    """Print prime numbers with specified limit(Second approach)"""

    print(f"Prime numbers between 1 and {limit} (Second approach):")
    for number in range(1, limit + 1):
        if number <= 1:
            is_prime = False
        elif number <= 3:
            is_prime = True
        elif number % 2 == 0 or number % 3 == 0:
            is_prime = False
        else:
            is_prime = True

            divisor = 5
            while divisor <= number**0.5:
                if number % divisor == 0 or number % (divisor + 2) == 0:
                    is_prime = False
                    break
                divisor += 6
        if is_prime:
            print(number, end=", ")


if __name__ == "__main__":
    limit = 50
    print_prime_numbers(limit)
    print()
    print_prime_numbers1(limit)
