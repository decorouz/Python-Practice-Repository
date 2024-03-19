"""Calculalting pi.

The mathematically significant number pi (π or 3.14159…) can be derived
using Leibniz formula. It posits that the convergence of the following 
infinite series is equal to pi:

π = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11...
"""


def calculate_pi(n_term: int) -> float:
    """Calculate pi(π) from Leibniz formula.

    Parameters
    ----------
    n_term: int
        Number of terms in a series

    Returns
    -------
        The value of pi.
    """
    numerator: float = 4.0
    denominator: float = 1.0
    operator: float = 1.0
    pi: float = 0
    for _ in range(n_term):
        pi += operator * numerator / denominator
        denominator += 2
        operator *= -1
    return pi


if __name__ == "__main__":
    print(calculate_pi(100003))
