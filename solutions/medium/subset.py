"""A recursive function that will output all the subsets of a set of n
elements (without repeating any subsets)"""


def subset(num_seq: list[int], n: int = 0, lst=None) -> list[list[int]]:
    """Generate all subsets of a given sequence.

    Parameters
    ----------
    my_set : list[int]
        Given sequence of integers
    n : int, default zero
        Minimum number of elements in a subset
    lst : list, optional
        subset placeholder, by default None

    Returns
    -------
    list[list[int]]
        Subsets of set of n elements without duplicates.
    """
    if not lst:
        lst = []

    for i in num_seq[n - 1 :]:
        lst.append(num_seq[: n - 1] + [i])
    if num_seq:
        subset(num_seq[1:], n, lst)
    return lst


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    length = 3
    print(subset(data, n=length))
