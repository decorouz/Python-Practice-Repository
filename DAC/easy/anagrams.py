def anagrams(word, words):
    return [anagram for anagram in words if sorted(word) == sorted(anagram)]


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])

# = > ['aabb', 'bbaa']

# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
# # = > ['carer', 'racer']

# anagrams('laser', ['lazing', 'lazy',  'lacer'])
# = > []
