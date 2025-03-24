import string
from pathlib import Path


def lettercount(filename: str = "./data/random_polish_text.txt"):
    """
    Count the occurrences of each letter in a text file.

    Reads a text file, converts all letters to lowercase, and counts the
    occurrences of each ASCII letter.
    """
    file_path = Path(filename)
    letter_counts = {}

    with file_path.open("r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            for letter in line.lower():
                if letter.isupper():
                    letter = letter.lower()
                if letter in string.ascii_lowercase:
                    if letter in letter_counts:
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1

    return letter_counts


# ---------
# more pythonic version that cannot be migrated to cython:
# ---------
# from collections import Counter
# from pathlib import Path
# import string
#
#
# def lettercount(filename: str = "./data/random_polish_text.txt"):
#     file_path = Path(filename)
#
#     with file_path.open("r", encoding="utf-8") as file:
#         text = file.read().lower()
#
#     # Filter only lowercase ASCII letters and count them
#     letter_counts = Counter(
#         letter for letter in text
#         if letter in string.ascii_lowercase
#     )
#
#     return dict(letter_counts)
