from time import time


def prime_sieve(n):
    "Returns a list of all primes <= n."
    primes = []
    a = [True] * n
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n, i):
                a[j] = False

    return set(primes)


PRIMES = prime_sieve(10000000)


def is_prime(x):
    """Returns true if x is prime."""
    if x <= 10000000:
        return x in PRIMES
    else:
        i = 2
        while i*i <= x:
            if x % i == 0:
                return False
            i += 1
        return True


def is_pandigital(x):
    """
    Returns true if the number x is n-digit pandigital where n is the length
    of x.
    """
    s = str(x)
    if len(s) > 9:
        return False

    digit_set = set(int(char) for char in s)
    for i in range(len(s)):
        if i + 1 not in digit_set:
            return False

    return True


def main():
    start = time()
    pandigital_primes = []
    # All 8 and 9 digit pandigitals are divisible by 3, and so not prime.
    for x in xrange(2143, 10000000, 2):
        if is_pandigital(x) and is_prime(x):
            pandigital_primes.append(x)
    print max(pandigital_primes)
    print time() - start


if __name__ == "__main__":
    main()
