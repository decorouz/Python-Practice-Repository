# You want to iterate over all the possible combinations and permutations of a collectio of items

items = ["a", "b", "c"]
from itertools import permutations
from itertools import combinations

for p in permutations(items):
    print("Permutation", p)

for p in permutations(items, 2):
    print("Permutation of smaller length", p)


for c in combinations(items, 2):
    print("Combination of items", c)
