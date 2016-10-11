def prime_sieve(n):
    """Returns a list of all primes <= n."""
    primes = []
    a = [True] * n
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n, i):
                a[j] = False

    return primes


def is_trunctable_prime(n):
    """Returns True if n is a trunctable prime."""
    if n < 10 or n not in primes:
        return False

    s = str(n)
    for i in range(1, len(s)):
        if int(s[i:]) not in primes or int(s[:-i]) not in primes:
            return False
    return True


digit_primes = [2, 3, 5, 7]
primes = prime_sieve(1000000)
trunctable_primes = [10*x + y for x in digit_primes for y in digit_primes if is_trunctable_prime(10*x + y)]

i = 0
while len(trunctable_primes) < 11:
    for x in digit_primes:
        for y in digit_primes:
            if is_trunctable_prime(int(str(x) + str(i) + str(y))):
                trunctable_primes.append(int(str(x) + str(i) + str(y)))
    i += 1
    print i

print trunctable_primes
print sum(trunctable_primes)
