def permutations(string, i=0):
    if i == len(string):
        "".join(string)

    for j in range(i, len(string)):

        words = [c for c in string]

        # swap
        words[i], words[j] = words[j], words[i]

        permutations(words, i + 1)


print(permutations('a'))
