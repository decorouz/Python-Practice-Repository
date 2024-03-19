"""One time-pad.

A one-time pad is a way of encrypting a piece of data by 
combining it with meaningless random dummy data in such a way 
that the original cannot be reconstituted without
access to both the product and the dummy data.
"""

from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    """Generate custom length bytes.

    Parameters
    ----------
    length: int
        Desired number of bytes

    Returns
    -------
        Bit strings from converted bytes
    """
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    """Perform encryption.

    Parameters
    ----------
    original
        Data to be encrypted

    Returns
    -------
        dummy and encrypted data
    """
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    """Perform decryption."""
    decrypted: int = key1 ^ key2  # XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
