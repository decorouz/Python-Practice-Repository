def word_summary(words: list) -> tuple[int, int, float]:
    """Takes a list of word. Return a tuple containing 3 integers;
    representing the length of shortest word, the length of the
    longest word, and the average word length
    """

    word_lengths = [len(word) for word in words]

    return min(word_lengths), max(word_lengths), sum(word_lengths) / len(word_lengths)


word_list = ["games", "hallelujah", "providences"]
print(word_summary(word_list))
