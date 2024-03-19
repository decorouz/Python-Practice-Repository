def caeser_cipher(character, rotate_by=3):
    """Create a caeser cipher from a character string.

    Parameters:
    ----------
    character: string
        String of characters
    rotate_by: int
        number of times to rotate by
    Return
    ------
    Scrambled character string
    """
    character = character.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if character not in alphabet:
        return character
    rotation_pos = ord(character) + rotate_by
    # if rotation_pos is less than ord(z)
    if rotation_pos <= ord(alphabet[-1]):
        return chr(rotation_pos)
    # if rotation_pos is greater than ord(z)
    return chr(rotation_pos - len(alphabet))


# Test
message_string = "Admide23"
encrypted_msg = map(caeser_cipher, message_string)
result = "".join(encrypted_msg)
print(result)
