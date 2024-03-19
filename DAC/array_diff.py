# My solutions
def array_diff(a, b):
    """Subtracts one list from another and returns the result.

    Removes all values from list a, which are present in list b keeping their order.

    Parameter
    ---------
        a (array): [list of numbers]
        b (array): [list of numbers]
    Return:
        New List
    """
    transformed_list = a
    for item in b:
        while item in a:
            a.remove(item)
    return transformed_list


# Most clever solution found online
def clever_soltuon(a, b):
    return [x for x in a if x not in b]


# array_diff([1, 2], [2])
clever_soltuon([1, 2], [2])
