"""Singly Linked Lists

Is a collection of nodes that collectively form a linear sequence
Each node stores a reference to an object that is an element of the sequence,
as well as a reference to the next node of the list
"""

# Implementing a Stack with Linked List
class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass

class LinkedStack:
    """LIFO stack implementation using singly linked list"""

    class _Node:
        """Non public class for storing a singly linked list"""
        __slot__ = "_element", "next"                       # manage memory
        def __init__(self, element, next) -> None:
            self._element = element
            self.next = next

    #--------- stack methods ------------#
    def __init__(self) -> None:
        """Create an empty stack"""
        self._head = None               # reference to the head of the node
        self._size = 0                  # No of stack elements

    def __len__(self):
        """Return the number of element in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but not remove the element at the top

        Raise an exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack

        Raise an exception if empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head.next
        self._size -= 1
        return answer