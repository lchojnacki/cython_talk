def allocation(size: int = 999_999) -> list[int]:
    """
    Allocate a list of integers and initialize it.

    Creates a list of a given size and populates it with even numbers.
    """
    numbers = [0] * size
    for i in range(size):
        numbers[i] = i * 2
    return numbers
