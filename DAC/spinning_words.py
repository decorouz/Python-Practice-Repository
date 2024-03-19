# First solution
def spin_words(sentence: str) -> str:
    """Given a string of words, spin the words with five or more characters"""
    spin_sentence = []
    words = sentence.split(" ")
    for word in words:
        if len(word) >= 5:
            spin_sentence.append(word[::-1])
        else:
            spin_sentence.append(word)
    return " ".join(spin_sentence)


# Clear solution


def spin_words2(sentence):
    spin_sentence = [
        word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")
    ]
    return " ".join(spin_sentence)


print(spin_words2("Hey fellow warriors"))
print(spin_words2("Welcome"))
print(spin_words2("This is a test"))
print(spin_words2("This is another test"))
