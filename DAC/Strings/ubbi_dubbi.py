import string


def ubbu_dubbi(word):
    """Ask the user to enter a word,
and return the word's translation into Ubbi Dubbi.
If the input word is capitalized, then the output
word should be, too.
    """

    output = []
    for letter in word:
        if letter.isupper():
            if letter in "aeiou".upper():
                output.append(f"Ub{letter.lower()}")

        elif letter in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    return "".join(output)


print(ubbu_dubbi("octopus"))


# An even better solution
def ubbi_dubbi(word):
    output = []

    for letter in word:
        if letter in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)
    if word[0] in string.ascii_uppercase:
        output[0] = output[0].capitalized()

    return "".join(output)
