class MyQueue:
    def __int__(self):
        self.in_stack = []      # tail for insertion
        self.out_stack = []     # head for extraction

    def __len__(self):
        return len(self.in_stack) + len(self.out_stack)

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if not self.out_stack:      # head is empty
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return self.out_stack.pop()


# Implementing Queue with a LinkedList
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def add_first(self, item):
        new_node = ListNode(item)
        self._head = new_node.next

    def add_last(self, item):
        if self._head is None:
            self.add_first(item)
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = ListNode(item)

    def remove_first(self):
        item = self._head.data
        self._head = self._head.next
        return item

    def remove_last(self):
        if self._head.next is None:
            self.remove_first()
        else:
            current_node = self._head
            while current_node.next.next is not None:
                current_node = current_node.next
            item = current_node.link.data
            current_node.next = None
            return item