def pig_latin(word:str):
    """Giving a word, transfer the initial consonant or consonant clusters
    of each word to the end of the word and adding a vocalic syllable: so pig latin
    becomes igpay atinlay"""
    if len(word.split()) > 1:
        result = []
        for item in word.split():
            result.append(util_func(item))
        return " ".join(result)
    return util_func(word)


def util_func(word:str):
    """Check if the letter is vowel"""
    word = word.lower()

    vowel = "aeiou"

    if word[0] in vowel:
        return f"{word}way"

    # find the index of the first vowel
    first_vowel = 0
    for i, letter in enumerate(word):
        if letter in vowel:
            first_vowel = i
            break

    return f"{word[first_vowel:]}{word[:first_vowel]}ay"


# Test the function with some words
word1 = "pig Latin"


print(pig_latin(word1)) # igpay atinlay
