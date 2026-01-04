# primes.py

def is_prime(n: int):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_primes(limit: int):
    """Generate primes using a simple Sieve of Eratosthenes"""
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]

    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(limit + 1) if sieve[i]]
