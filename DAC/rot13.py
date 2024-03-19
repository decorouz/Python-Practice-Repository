import string


def rot13(message):
    new_msg = []
    for letter in message:
        new_msg.append(new_letter(letter))

    return "".join(new_msg)


def new_letter(letter):
    key = 13
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    if str(letter).isdigit():
        return letter
    if letter in lower:
        rotate_pos = ord(letter) + key
        return chr(rotate_pos) if rotate_pos <= ord(lower[-1]) else chr(rotate_pos - len(lower))

    elif letter in upper:
        rotate_pos = ord(letter) + key
        return chr(rotate_pos) if rotate_pos <= ord(upper[-1]) else chr(rotate_pos - len(upper))

    return letter


print(rot13("NibvqMfhpprffMngMnyyMpbfgfM"))
