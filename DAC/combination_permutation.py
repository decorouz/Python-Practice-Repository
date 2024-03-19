# You want to iterate over all the possible combinations and permutations of a collectio of items

items = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
correct_pass = ("4", "7", "5", "0", "2", "1")
attempt = 5

from itertools import permutations
from itertools import combinations

# for p in permutations(items):
#     print("Permutation", p)
counter = 0
for p in permutations(items, 6):
    counter = counter + 1
    if p == correct_pass:
        print(counter)
        print(p)


#
# for c in combinations(items, 2):
#     print("Combination of items", c)
