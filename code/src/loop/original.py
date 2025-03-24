def loop(n: int = 10_000_000) -> int:
    """
    Calculate the sum of numbers up to n.

    Iterates through numbers from 0 to n-1 and calculates their sum.
    """
    result = 0
    for i in range(n):
        result += i
    return result
