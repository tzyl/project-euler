# To minimize n / phi(n) we need few large prime factors.
# A single prime would not work as then phi(n) = n - 1 which cannot be a
# permutation of n.
# If we have two distinct primes then we can reduce to:
# phi(n) = (p1 - 1) * (p2 - 1)
# Find two distinct primes close to sqrt(1e7) ~= 3162.
# Try pairs between 2000 to 5000.


def prime_sieve(n):
    """Returns a set of all primes <= n."""
    primes = []
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n + 1, i):
                a[j] = False

    return primes


def is_permutation(n1, n2):
    """Retruns True if integers n1 and n2 are permutations of each other."""
    return sorted(str(n1)) == sorted(str(n2))


if __name__ == '__main__':
    # First generate primes between 2000 and 5000.
    primes = prime_sieve(5000)
    i = 0
    while primes[i] < 2000:
        i += 1
    primes = primes[i:]
    # Now try pairs to find the best totient permutation.
    best_n = 1
    best_phi = 1
    best_ratio = float("inf")
    for i in xrange(len(primes)):
        for j in xrange(i + 1, len(primes)):
            n = primes[i] * primes[j]
            if n < 1e7:
                phi = (primes[i] - 1) * (primes[j] - 1)
                ratio = float(n) / phi
                if is_permutation(n, phi) and ratio < best_ratio:
                    best_n, best_phi, best_ratio = n, phi, ratio
    print best_n, best_phi, best_ratio
