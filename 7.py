def prime_sieve(n):
    """Returns a list of all primes <= n."""
    primes = []
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n + 1, i):
                a[j] = False

    return primes


if __name__ == '__main__':
    primes = prime_sieve(1000000)
    print primes[10000]
