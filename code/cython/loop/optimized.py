import cython


def loop(n: cython.int = 10_000_000) -> cython.long:
    """
    Calculate the sum of numbers up to n.

    Iterates through numbers from 0 to n-1 and calculates their sum.
    """
    result: cython.long = 0
    i: cython.int
    for i in range(n):
        result += i
    return result
