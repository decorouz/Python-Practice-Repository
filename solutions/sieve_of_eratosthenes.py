"""The Sieve of Eratosthenes.

An algorithm used to generate all prime numbers smaller than an integer.
The method is to take increasingly larger prime numbers, and mark 
their multiples as composite.

For example, to find all primes less than 100, we would first mark 
[4, 6, 8, ...] (multiples of two),then [6, 9, 12, ...] 
(multiples of three), and so on. Once we have done this for all primes 
less than N,the unmarked numbers that remain will be prime.

Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely 
(that is, without taking N as an input).

"""
from typing import Generator, Any


def seive_of_eratosthenes(num: int) -> Generator[int, Any, None]:
    """Generate all prime numbers less than given num.

    Parameters
    ----------
    N: int
        A positive integer
    Return
    ------
        generator: generator containing list of primes
    """
    # initialize a list of Trues
    true_list = [True for _ in range(num)]
    true_list[0] = true_list[1] = False

    for i, isprime in enumerate(true_list):
        if isprime:
            yield i
            for val in range(i * i, num, i):
                true_list[val] = False


if __name__ == "__main__":
    result = seive_of_eratosthenes(100)
    print(result)
