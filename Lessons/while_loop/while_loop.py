"""Simple Examples of while loops"""

# Calculate all the numbers from 1 to 100

N = 100
COUNTER = 1
TOTAL_SUM = 0

while COUNTER <= N:
    TOTAL_SUM += COUNTER
    COUNTER += 1

# print(f"The sum of 1 until {N} is {TOTAL_SUM}")


# Write a program, which asks for the initial balance K0 and for the interest rate.
# The program shall calculate the new capital K1 after one year including the interest.
# Extend the program with a while-loop, so that the capital Kn after a period of n years
# can be calculated.

K = float(input("Starting balance? "))
P = float(input("Interest rate? "))
N = float(input("Number of year? "))

# Initialize the number of years
n = 0
while n <= N:
    # calculate the new capital after one year
    K += K * P / 100
    n += 1
    print(n, K)
print(f"Capital after {N} yrs: {K}")
