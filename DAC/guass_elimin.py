## module GuassElimin
"""
Gauss Elimination Method.
It is the most familiar method for solving simultenous equations.
It consists of two parts: the elimination phase and solution phase.
x = guass_elimin(a, b).
    Solve [a]{b} = {x} by Gauss Elimination
"""
import numpy as np


def gauss_elimin(a, b):
    """Gauss Elimination method.

    The function combines the elimination and back substitution phase.
    """

    n = len(b)
    # Elimination phase
    for k in range(0, n+1):
        for i in range(k+1, n):
            if a[i, k] != 0.0:
                lam = a[i, k]/a[k, k]
                a[i, k+1:n] = a[i, k+1:n] - lam*a[k, k+1:n]
                b[i] = b[i] - lam*b[k]

    #substitution phase
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b
