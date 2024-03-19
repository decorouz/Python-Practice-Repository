def transpose_string(list_of_words):
    """Given a list of strings, each of which contains
        multiple words, transpose them.

    Args:
        list_of_words (list): ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']

    Returns:
        ['abc jkl stu', 'def mno vwx', 'ghi pqr yz'].
    """
    output = zip(*[s.split(" ") for s in list_of_words])
    return [" ".join(t) for t in output]


result = transpose_string(['abc def ghi', 'jkl mno pqr', 'stu vwx yz'])

print(result)
