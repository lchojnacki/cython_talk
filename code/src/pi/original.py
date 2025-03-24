def pi(loops: int = 999_999) -> float:
    """
    Estimate the value of pi using the Nilakantha series.

    This function approximates pi by summing a finite number of terms
    of the Nilakantha series. The number of terms is determined by
    the input 'loops'.

    :param loops: The number of terms to include in the summation.
    :return: The estimated value of pi.
    """
    pi_estimate: float = 3.0
    for n in range(1, loops + 1):
        sign: int = -((-1) ** n)
        term = 4 / (2 * n * (2 * n + 1) * (2 * n + 2))
        pi_estimate += sign * term

    return pi_estimate
