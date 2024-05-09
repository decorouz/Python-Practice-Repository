# Print numbers from 1 to 42, but for multiples of 3,
# print "Fizz," and for multiples of 5, print "Buzz."
# For numbers that are multiples of both 3 and 5, print "FizzBuzz."


for number in range(1, 42 + 1):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: FizzBuzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(number)
