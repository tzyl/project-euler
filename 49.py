def prime_sieve(n):
    """Returns a list of all primes <= n."""
    primes = []
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n, i):
                a[j] = False

    return set(primes)


def permutations(lst):
    """Returns all permutations in a list of the string elements in lst."""
    if len(lst) <= 1:
        return lst

    p = []

    for i, elt in enumerate(lst):
        p.extend([elt + perm for perm in permutations(lst[:i] + lst[i+1:])])

    return p


primes = prime_sieve(10000)
i = 1000
while i < 10000:
    if i in primes:
        perms = set(permutations([c for c in str(i)]))
        for j in xrange(1, (9999 - i) / 2):
            if i + j in primes and str(i + j) in perms:
                if i + 2*j in primes and str(i + 2*j) in perms:
                    print i, i + j, i + 2*j
    i += 1
