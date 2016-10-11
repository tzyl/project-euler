#def totient(n):
#    """
#    Returns the number of numbers less than or equal to n which are relatively
#    prime to n.
#    """
#    if n < 2:
#        return 0
#
#    products = []
#    for prime in primes:
#        if prime > n:
#            break
#        elif n % prime == 0:
#            products.append(1 - 1.0 / prime)
#    return int(n * reduce(lambda x, y: x * y, products))


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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


primes = prime_sieve(1000000)

#totient_maximum = (0, 0)
#for n in xrange(2, 1000001):
#    val = float(n) / totient(n)
#    if val > totient_maximum[1]:
#        totient_maximum = (n, val)
#        print totient_maximum

# We find that the largest quotient is simply the distinct product of the
# smallest consecutive primes.
n = 1
i = 0
while n * primes[i] <= 1000000:
    n *= primes[i]
    i += 1
print n
