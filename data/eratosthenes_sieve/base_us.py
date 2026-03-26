def eratosthenes_sieve(limit):
    """
    Returns a list of all prime numbers up to and including limit
    using the Sieve of Eratosthenes algorithm.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    current_number = 2
    while current_number * current_number <= limit:
        if is_prime[current_number]:
            multiple = current_number * current_number
            while multiple <= limit:
                is_prime[multiple] = False
                multiple += current_number
        current_number += 1

    prime_list = [number for number in range(2, limit + 1) if is_prime[number]]
    return prime_list