"""SIMPLE CRYPTOGRAPHY.

The Caesar cipher is a simple way to obscure a message
written in a language that forms words with an alphabet.
"""


def _transform(original, code):
    msg = list(original)  # turn message to a list
    print(msg)
    for i, _ in enumerate(msg):
        if msg[i].isupper():
            j = ord(msg[i]) - ord("A")
            msg[i] = code[j]
    return "".join(msg)


class CaesarCipher:
    """Class for doing encryption and decryption using Caeser cipher."""

    def __init__(self, shift: int) -> None:
        """Construct Caeser cipher using given integer shift for rotation.

        Parameters
        ----------
        shift: int
            An arbitrary rotational shift
        """
        encoder = [""] * 26  # temp array for encryption
        decoder = [""] * 26  # temp array for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message) -> str:
        """Return string representing the encrypted message"""
        return _transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret"""
        return _transform(secret, self._backward)


if __name__ == "__main__":
    cipher = CaesarCipher(20)
    MESSAGE = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    CODED = cipher.encrypt(MESSAGE)
    print("Secret: ", CODED)
    # ANSWER = cipher.decrypt(CODED)
    # print("Message: ", ANSWER)
