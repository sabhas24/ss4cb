def euclidean_gcd(first_number, second_number):
    """
    Returns the greatest common divisor of first_number and second_number
    using the Euclidean algorithm.
    """
    dividend = first_number
    divisor = second_number

    while divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder

    return dividend