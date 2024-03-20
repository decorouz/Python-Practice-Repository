"""Suppose you want to create some helper function for class that contains some logic but is not a property of the class"""

from typing import Any, Iterable


class Multiply:
    def __init__(self, numbers: Iterable[int]) -> None:
        self.numbers = numbers
        self.result = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"Multiply {self.numbers}")
        self.checker(self.numbers)
        self.result = 1
        for num in self.numbers:
            self.result *= num
        print(self.result)

    @staticmethod
    def checker(numbers: list):
        """Ensure list of int"""
        for num in numbers:
            if not isinstance(num, int):
                raise ValueError("Accepts only integers")


valid = Multiply([1, 2, 3])
# invalid = Multiply([1, 2, "three"])
valid()
# invalid()
