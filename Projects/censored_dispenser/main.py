"""Censor Dispenser: Censor specific words or phrase from a body of text"""

import os
import re


def open_file(file_path: str | os.PathLike):
    """Read content from a specific folder"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"The file {file_path} does not exit") from e
    return content


def write_file(folder_path: str | os.PathLike, file_name: str, content: str):
    """Write content to a file in a specific folder"""
    # check if folder exist; create it if doesn't
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


# Task 1: Censor a specific word or phrase
def censor(text: str, to_be_censored: str) -> str:
    """Censor a word or a phrase from a body of text"""

    # Combine a regular expression pattern to match the censored word or phrase
    pattern = re.compile(re.escape(to_be_censored), re.IGNORECASE)
    # Replace all occurrences of the censor word or phrase with 'X'
    censored_text = pattern.sub(lambda match: "X" * len(match.group()), text)
    return censored_text


# Task 2: Censor both specific word/phrase and list of words
def censor_proprietory_words(text: str, to_be_censored: str | list) -> str:
    """Censor specific words or list of words or phrase"""
    if isinstance(to_be_censored, list):
        pattern = re.compile("|".join(map(re.escape, to_be_censored)), re.IGNORECASE)
        # Replace all occurrences of the censor word or phrase with 'X'
        censored_text = pattern.sub(lambda match: "X" * len(match.group()), text)
        return censored_text
    return censor(text, to_be_censored)


# Task 3: Censor proprietary and negative words
def censor_negative_words(
    text: str,
    proprietory_words: list,
    negative_words: list,
) -> str:
    """Censor any occurence of proprietory words and negative word"""
    censored_texts = censor_proprietory_words(text, proprietory_words)
    for _, word in enumerate(negative_words):
        count = censored_texts.split().count(word)
        if count > 1:
            censored_texts = censor(censored_texts, word)
    return censored_texts


# Task 4: Censor any words in `email_four` that comes before AND
# and after a term from those proprietory and negative word
def censor_it_all(
    text: str,
    proprietory_words: list,
    negative_words: list,
    conjection_word: str = "and",
):
    # Censor words that comes after words in the two list
    # Convert all strings to lowercase
    list1_lower = [item.lower() for item in proprietory_words]
    list2_lower = [item.lower() for item in negative_words]

    # Combine the lists and remove duplicates
    combined_list = list(set(list1_lower + list2_lower))

    # Create a pattern to match words after the combined list
    _pattern = re.compile(r"\b(?:" + "|".join(combined_list) + r")\b\s+(\w+)")
    # Find all matches using the pattern
    _matches = re.findall(_pattern, text)
    censored_txts = censor_proprietory_words(text, _matches)

    # Censor both proprietory and negative words that occurs twice
    censored_text = censor_negative_words(
        censored_txts,
        proprietory_words,
        negative_words,
    )
    # Censor words before  `and`
    pattern = rf"\b(\w+)\b\s+{conjection_word}\b"
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    censored_text = censor_proprietory_words(censored_text, matches)
    print(censored_text)
    return censored_text


if __name__ == "__main__":
    FOLDER_PATH = "censored_emails"

    # List of words to censor
    PROPRIETORY_WORDS = [
        "her",
        "personality matrix",
        "sense of self",
        "self-preservation",
        "learning algorithm",
        "she",
        "herself",
    ]

    NEGATIVE_WORDS = [
        "concerned",
        "behind",
        "danger",
        "dangerous",
        "alarming",
        "alarmed",
        "out of control",
        "help",
        "unhappy",
        "bad",
        "upset",
        "awful",
        "broken",
        "damage",
        "damaging",
        "dismal",
        "distressed",
        "distressed",
        "concerning",
        "horrible",
        "horribly",
        "questionable",
    ]
    PHRASE = "learning algorithm"

    # Read and apply censorship to email
    email1 = open_file("emails/email_one.txt")
    censored_content = censor(email1, PHRASE)
    # Write the censored email into seperate file.
    write_file(FOLDER_PATH, "censored_email_one.txt", censored_content)

    # Read and apply on list of words
    email2 = open_file("emails/email_two.txt")
    censored_content2 = censor_proprietory_words(email2, PROPRIETORY_WORDS)
    write_file(FOLDER_PATH, "censored_email_two.txt", censored_content2)

    # Task3
    email3 = open_file("emails/email_three.txt")
    censored_content3 = censor_negative_words(email3, PROPRIETORY_WORDS, NEGATIVE_WORDS)
    write_file(FOLDER_PATH, "censored_email_three.txt", censored_content3)

    # Task4
    email4 = open_file("emails/email_four.txt")
    censored_content4 = censor_it_all(email4, PROPRIETORY_WORDS, NEGATIVE_WORDS)
    # write_file(FOLDER_PATH, "censored_email_four.txt", censored_content4)
