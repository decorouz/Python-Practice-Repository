class ListNode:
    def __init__(self, data, prev=None, link=None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:  # store two links in a node.
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def add_first(self, item):
        if len(self) == 0:
            self._head = self._tail = ListNode(item, None, None)
        else:
            new_node = ListNode(item, None, self._head)
            self._head.prev = new_node
            self._head = new_node
        self._length += 1

    def add_last(self, item):
        if len(self) == 0:
            self._head = self._tail = ListNode(item, self._tail, None)
        else:
            new_code = ListNode(item, self._tail, None)
            self._tail.link = new_code
            self._tail = new_code
        self._length += 1

    def __len__(self):
        return self._length

    def __iadd__(self, other):
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail
            self._length = self._length + other._length
        other.__init__()
        return self


L = DoublyLinkedList()
[L.add_last(i) for i in range(11)]
B = DoublyLinkedList()
[B.add_last(i + 11) for i in range(10)]
L += B
n = L._head
while n is not None:
    print(n.data, end=" ")
    n = n.link
