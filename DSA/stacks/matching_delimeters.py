"""An important task when processing arithmatic expressions is to make
sure their delimiting symbols match up correctly.
The code below is an example of the implementation of such algorithm.
"""

from dataclasses import dataclass, field


@dataclass
class ArrayStack:
    _data: list = field(default_factory=list)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        return self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()


def is_match(expr: str) -> bool:
    """Return True if all delimiters are properly match;False otherwise

    Args:
        expr (str): sequence of characters with delimiters
    """
    left = "({["
    right = ")}]"

    S = ArrayStack()
    for char in expr:
        if char in left:
            S.push(char)
        elif char in right:
            if S.is_empty():
                return False
            if right.index(char) != left.index(S.pop()):
                return False
    return S.is_empty()


def is_match_using_dict(chars):
    s = ArrayStack()
    d = {")": "(", "}": "{", "]": "["}
    for c in chars:
        if c in d.values():
            s.push(c)
        elif c in d.keys():
            if s.is_empty():
                return False
            if d[c] != s.pop():
                return False
    return s.is_empty()


if __name__ == "__main__":
    strs = "[(5+x)-(y+z)]"
    strs2 = "()"
    print(is_match_using_dict(strs))
    print(is_match(strs2))
