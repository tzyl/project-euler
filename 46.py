import itertools


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


k = 1000
primes = prime_sieve(k)
squares = set(x*x for x in range(1, int(k**0.5) + 1))
i = 3
while True:
    if i > k:
        k += 1000
        print k
        primes = prime_sieve(k)
        squares = set(x*x for x in range(1, int(k**0.5) + 1))
        continue
    elif i in primes:
        i += 2
        continue

    found_decomposition = False
    for prime, square in itertools.product(primes, squares):
        if i == prime + 2*square:
            found_decomposition = True
            break

    if not found_decomposition:
        print i
        break

    i += 2
