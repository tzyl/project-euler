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


def is_prime(x):
    if x < 2:
        return False
    elif 2 <= x <= 3:
        return True
    else:
        for y in xrange(2, int(x ** 0.5) + 1):
            if x % y == 0:
                return False
        return True


primes = prime_sieve(1000000)

# Denote side length of square spiral by n.
n = 7
p = 8
num = 49
prime_ratio = float(p) / (2*n - 1)

while prime_ratio > 0.1:
    n += 2
    for i in range(4):
        num += n - 1
        if is_prime(num):
            p += 1
            print num
    prime_ratio = float(p) / (2*n - 1)

print n, prime_ratio
