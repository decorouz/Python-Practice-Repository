"""Implementing a Stack Using a Python List
"""


class Empty(Exception):
    """Error attempting to access an element from an empty container"""

    pass


class ArrayStack:
    """LIFO stack implementation using Python list"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


# ==== Example usage of created Stack Abstract Data Structure
def reverse_file(f_name):
    S = ArrayStack()
    original = open(f_name)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(f_name, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()


# reverse_file("logfile.txt")
