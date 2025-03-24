import cython
from cython.cimports.libc.stdlib import free, malloc


def allocation(size: cython.int = 999_999) -> list[int]:
    """
    Allocate a list of integers and initialize it.

    Creates a list of a given size and populates it with even numbers.
    """
    numbers: cython.p_int = cython.cast(
        cython.p_int, malloc(size * cython.sizeof(cython.int))
    )

    if not numbers:
        raise MemoryError("Memory allocation failed")

    try:
        i: cython.int
        for i in range(size):
            numbers[i] = i * 2

        return list(x for x in numbers[:size])  # noqa: C400
    finally:
        free(numbers)
