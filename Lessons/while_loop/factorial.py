# Write a Python program that calculates the factorial of a number entered by the user using a while loop. The factorial of a non-negative integer n, denoted in mathematics as n!, is the product of all positive integers from 1 to n. For example, 5! (read as "5 factorial") is equal to 5 * 4 * 3 * 2 * 1, which is 120.

n = int(input("Enter a Number(Positive Integer): "))


counter = 1
factorial = 1

while counter <= n:
    factorial *= counter
    counter += 1
print(f"{n}! 5= {factorial}")
