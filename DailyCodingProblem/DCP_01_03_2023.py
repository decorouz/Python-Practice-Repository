"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, 
the unmarked numbers that remain will be prime.

Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

"""
from typing import List


def seive_of_eratosthenes(N: int) -> List:
    """generate all prime numbers less than N

    :param N: Number
    :return List: list of prime numbers less than N
    """
    # initialize a list of Trues
    true_list = [True for _ in range(N)]
    true_list[0] = true_list[1] = False

    for (i, isprime) in enumerate(true_list):
        if isprime:
            yield i
            for n in range(i * i, N, i):
                print(n)
                true_list[n] = False
