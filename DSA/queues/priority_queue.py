"""Queue that sorts items by priority.

To implement a queue that sorts items by a given priority and always
return item with the highest priority on each pop operation
"""
import heapq


class PriorityQueue:
    """Sort items by given priority"""

    def __init__(self):
        self._heap = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._heap, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """Extract the item with the highest priority"""
        return heapq.heappop(self._heap)[-1]


class Item:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"Item('{self._name}')"


q = PriorityQueue()
q.push(Item("Refined tiger"), 1)
q.push(Item("Turn off of a musical instrument"), 2)
q.push(Item("Voluptuous"), 38)

print(q.pop())
