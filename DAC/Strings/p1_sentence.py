
def p1_sentence(sentence:str)->str:
    """Takes a string containing several words
        separated by spaces.

    Args:
        sentence (string): space separated words

    Returns:
        string: Output on a single line of the translated word.
        `this is a test translation` would be `histay isway away estay ranslationtay`

    """
    sentence.lower()

    output = []
    for word in sentence.split():
        if word[0] in "aeiou":
            output.append(f"{word}way")
        else:
            output.append(f"{word[1:]}{word[0]}ay")
    return " ".join(output)


print(p1_sentence("this is a translation"))
