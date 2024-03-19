class MyMinHeap:
    def __init__(self, items):
        self.heap = [0]  # Index 0 will be ignored
        self.rank = {}
        for x in items:
            self.push(x)

    def __len__(self):
        """Returns the number of elements in the heap"""
        return len(self.heap) - 1

    def push(self, x):
        assert x not in self.rank
        i = len(self.heap)
        self.heap.append(x)  # add a new leaf
        self.rank[x] = i
        self.up(i)  # maintain heap other

    def pop(self):
        root = self.heap[1]
        del self.rank[root]
        x = self.heap.pop()  # remove last leaf
        if self:  # if heap is not empty
            self.heap[1] = x  # move the last leaf
            self.rank[x] = 1  # to the root
            self.down(1)  # maintain heap other
        return root

    def up(self, i):
        x = self.heap[i]
        # self.heap[i//2] parent node.
        while (
            i > 1 and x < self.heap[i // 2]
        ):  # while the element is not the root or th left elemment
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            # move the index to the parent to keep the properties
            i //= 2
        self.heap[i] = x  # insertion index found
        self.rank[x] = i

    def down(self, i):
        x = self.heap[i]
        n = len(self.heap)
        while True:
            left_child = 2 * i  # Climb down the tree
            right_child = left_child + 1
            if (
                right_child < n
                and self.heap[right_child] < x
                and self.heap[right_child] < self.heap[left_child]
            ):
                self.heap[1] = self.heap[right_child]
                self.rank[self.heap[right_child]] = i  # move right_child child up
                i = right_child
            elif left_child < n and self.heap[left_child] < x:
                self.heap[i] = self.heap[left_child]
                self.rank[self.heap[left_child]] = i  # move left_child child up
                i = left_child
            else:
                self.heap[i] = x  # insertion index found
                self.rank[x] = i
                return

    def update(self, old, new):
        """Change the value of a heap"""
        i = self.rank[old]
        del self.rank[old]
        self.heap[i] = new
        self.rank[new] = i
        if old < new:
            self.down(i)
        else:
            self.up(i)


my_heap = MyMinHeap([])
my_heap.push(5)
my_heap.push(6)
my_heap.push(7)
my_heap.push(9)
my_heap.push(13)
my_heap.push(11)
my_heap.push(10)
my_heap.update(6, 4)
print(my_heap.heap)
