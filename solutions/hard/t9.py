"""The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. 
We would like to make it easier to write a message to your friend using a sequence of keypresses 
to indicate the desired characters. The letters are mapped onto the digits as shown below. 
To insert the character B for instance, the program would press 22. 
In order to insert two characters in sequence from the same key,
the user must pause before pressing the key a second time. The space character ‘ ‘ 
should be printed to indicate a pause. For example, 2 2 indicates AA whereas 22 indicates B."""

t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz        mapping on the phone


def letter_to_digit(x):
    assert "a" <= x <= "z"
    return t9[ord(x) - ord("a")]


def code_word(word):
    """Returns corresponding sequence of digits"""
    return "".join(map(letter_to_digit, word))


def predictive_text(dic):
    total_weight = {}
    for word, weight in dic:
        prefix = ""
        for x in word:
            prefix += x
            if prefix in total_weight:
                total_weight[prefix] += weight
            else:
                total_weight[prefix] = weight
    prop = {}
    for prefix in total_weight:
        code = code_word(prefix)
        if code not in prop or total_weight[prop[code]] < total_weight[prefix]:
            prop[code] = prefix
    return prop


def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    return None
