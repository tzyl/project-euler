
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

    return primes


primes = prime_sieve(1000000)
most_consecutive = 21
most_consecutive_prime = 953

# Find an upper bound on the number of consecutive primes.
n = 1
while sum(primes[:n]) < 1000000:
    n += 1

for i, prime in enumerate(primes):
    k = most_consecutive
    while k <= n:
        if sum(primes[:k]) > prime:
            break
        j = 0
        while sum(primes[j:j+k]) < prime:
            j += 1
        if sum(primes[j:j+k]) == prime:
            most_consecutive = k
            most_consecutive_prime = prime
        k += 1

print most_consecutive_prime, most_consecutive
