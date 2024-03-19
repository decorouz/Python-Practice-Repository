"""The algorithm for the conjecture"""
# Start with any positive integer n.
# If n is even, divide it by 2.
# If n is odd, multiply it by 3 and add 1.
# Repeat the process with the calculated value as the new value of n,
# and continue until n becomes 1

# ? Write a program to print out the sequence of a number
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a valid positive integer!")
if n > 0:
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)


# ? How long is the sequence for the number 271114753?
SEQUENCE_LENGTH = 0
if n <= 0:
    print("Please enter a valid positive integer!")

if n > 0:
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        SEQUENCE_LENGTH += 1
print(f"The length of sequence: {SEQUENCE_LENGTH}")

# ? Write a program to print the lengths of the Collatz sequences for the numbers from 1 to 100.
COUNTER = 1
STOP_VALUE = 100
while COUNTER <= STOP_VALUE:
    n = COUNTER
    LENGTH_OF_SEQUENCE = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        LENGTH_OF_SEQUENCE += 1
    print(f"{COUNTER}: {LENGTH_OF_SEQUENCE}", end=",")
    COUNTER += 1
print()
