import cython
from cython.cimports.libc.stdio import fclose, fopen
from cython.cimports.libcpp.unordered_map import unordered_map
from cython.cimports.posix.stdio import getline


def lettercount(filename: bytes = b"./data/random_polish_text.txt"):
    """
    Count the occurrences of each letter in a text file.

    Reads a text file, converts all letters to lowercase, and counts the
    occurrences of each ASCII letter.
    """
    file = fopen(filename, b"r")

    if file is cython.NULL:
        return None

    buffer: cython.p_char = cython.NULL
    size: cython.size_t = 0
    read: cython.Py_ssize_t

    letter_counts: unordered_map[cython.char, cython.int]
    letter: cython.char

    while True:
        read = getline(cython.address(buffer), cython.address(size), file)
        if read == -1:
            break
        for letter in buffer:
            if 65 <= letter <= 90:
                letter = letter + 32
            if 97 <= letter <= 122:
                if letter_counts.find(letter) == letter_counts.end():  # noqa: F821
                    letter_counts[letter] = 1  # noqa: F821
                else:
                    letter_counts[letter] += 1  # noqa: F821

    fclose(file)

    return {chr(key): value for key, value in letter_counts}  # noqa: F821
