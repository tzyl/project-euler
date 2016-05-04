def prime_sieve(n):
    "Returns a list of all primes <= n."
    primes = []
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n, i):
                a[j] = False

    return set(primes)


# primes = prime_sieve(1000000)


def prime_factorisation(n):
    "Returns the prime factorisation of n in a list."
    p_factorisation = []
    primes = prime_sieve(n + 1)
    while n > 1:
        for prime in primes:
            if n % prime == 0:
                p_factorisation.append(prime)
                n /= prime
                break
    return p_factorisation


i = 210
found = False

while not found:
    print i
    for n in range(i, i+4):
        if len(set(prime_factorisation(n))) != 4:
            i = n + 1
            break
        if n == i + 3:
            found = True

print i
