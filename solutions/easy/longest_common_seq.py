"""Longest common subsequences.
Subsequence of a string `s` is a string `t` such that
the characters of `t` all appears in `s` in the same order.
For example `abc` is a subsequence of `xxxxxxaxxxxbxxxxcxxx`
"""


def recursive_lcs(x, y):
    if x == "" and y == "":
        return ""
    if x[-1] == y[-1]:
        return recursive_lcs(x[:-1], y[:-1]) + x[-1]
    return max([recursive_lcs(x[:-1], y), recursive_lcs(x, y[:-1])], key=len)


def dp_lcs(x, y):
    t = {}
    for i in range(len(x) + 1):
        t[(i, 0)] = ""
    for j in range(len(y) + 1):
        t[(0, j)] = ""

    for i, x in enumerate(x):
        for j, y in enumerate(y):
            if x == y:
                t[(i + 1, j + 1)] = t[(i, j)] + x
            else:
                t[(i + 1, j + 1)] = max([t[i, j + 1], t[(i + 1, j)]], key=len)
    return t[(len(x), len(y))]


print(dp_lcs("xxxxxxaxxxxbxxxxcxxx", "abc"))
