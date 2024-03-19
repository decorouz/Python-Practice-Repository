
def sum_intable(object_list):
    """Takes a list of python objects.
        Sum the objects that are int or can be converted into integer, ignoring orders"""
    return sum(val
               for val in object_list
               if isinstance(val, (int, float)))


print(sum_intable([1, 2, 3, 3.1,  'HELLO', 'WORLD']))
print(sum_intable([1, 2, 3, 4, 5, 6, "A", "B"]))
