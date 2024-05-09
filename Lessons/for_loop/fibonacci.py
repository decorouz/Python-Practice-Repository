# * Generate and print the first n numbers in the Fibonacci sequence using a for loop
# Iterating over list with range


def fibonacci(n: int) -> list[int]:
    """Generate fibonacci the first sequence up to nth term"""
    # Initialize the sequence with the first two terms
    fib_sequence = [0, 1]

    # generate the rest of the terms using a loop
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    fibo = fibonacci(n)
    print(fibo)
