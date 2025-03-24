import cython
from cython.parallel import prange


@cython.cdivision(True)
@cython.cpow(True)
@cython.profile(True)
@cython.linetrace(True)
def pi(loops: cython.int = 15) -> cython.double:
    """
    Estimate the value of pi using the Nilakantha series.

    This function approximates pi by summing a finite number of terms
    of the Nilakantha series. The number of terms is determined by
    the input 'loops'.

    :param loops: The number of terms to include in the summation.
    :return: The estimated value of pi.
    """
    pi_estimate: cython.double = 3.0
    n: cython.long

    for n in prange(1, loops + 1, nogil=True):
        sign: cython.short = -((-1) ** n)
        term: cython.double = 4.0 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
