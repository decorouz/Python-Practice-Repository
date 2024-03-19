"""The Towers of Hanoi.

Our goal is to move all of the discs from tower A to tower C 
given the following constraints:
    - Only one disc can be moved at a time.
    - The topmost disc of any tower is the only one available for moving.
    - A wider disc can never be atop a narrower disc.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """Stack Data Structure."""

    def __init__(self) -> None:
        self._container: list[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs = 20
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

# Fill the first tower with discs
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(
    disk: int,
    source: Stack[int],
    target: Stack[int],
    temp: Stack[int],
) -> None:
    """Solves the Tower of Hanoi problem recursively for three towers.

    Parameters
    ----------
    source
        The source tower from which the disks are to be moved.
    target
        The target tower to which the disks are to be moved.
    temp
        Other peg
    disk
        The number of disks to be moved
    """
    if disk == 1:
        target.push(source.pop())
    else:
        hanoi(disk - 1, source, temp, target)
        hanoi(1, source, target, temp)
        hanoi(disk - 1, temp, target, source)


if __name__ == "__main__":
    hanoi(num_discs, tower_a, tower_b, tower_c)
    print(tower_a)
    print(tower_b)
    print(tower_c)
