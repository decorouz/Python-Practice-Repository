"""Compression and decompression by example."""


class CompressedGene:
    """Internally stores the sequence of nucleotides as a bit string."""

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        """Perform compression.

        Parameters
        ----------
        gene: str
            Nucleotide in a gene
        """
        self.bit_string: int = 1  # start with a sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left by 2 bits
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid nucleotide:{nucleotide}")

    def decompress(self) -> str:
        """Perform decompression.

        Returns
        -------
            Sequence of characters A, C, G, and T.

        Raises
        ------
        ValueError
        """
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += "A"
            elif bits == 0b01:
                gene += "C"
            elif bits == 0b10:
                gene += "G"
            elif bits == 0b11:
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = (
        "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA"
        * 100
    )
    print(f"original is {getsizeof(original)} bytes")
    compressed: CompressedGene = CompressedGene(original)  # compress
    print(f"compressed is {getsizeof(compressed.bit_string)} bytes")
    print(compressed)  # decompress
    print(
        f"original and decompressed are the same: {original == compressed.decompress()}"
    )
