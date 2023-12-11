"""Given an array of strings, group the anagram together.
You can return the answer in any order.

Example: 
input = ["eat", "tea", "tan",  "ate", "nat", "bat]
output = [["bat], ["nat", "tan"], ["eat", "tea", "ate",]]
"""
from collections import defaultdict


class GroupAnagram:
    def group_anagram(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        output = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for value in anagram_map.values():
            output.append(value)
        return output


if __name__ == "__main__":
    input_str = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = GroupAnagram().group_anagram(input_str)
    print(result)
