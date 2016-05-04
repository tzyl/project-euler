from itertools import combinations


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


def replace_digits(x, new_digit, idxs):
    s = list(str(x))
    for idx in idxs:
        s[idx] = str(new_digit)
    return int("".join(s))


upper_bound = 1000000
primes = prime_sieve(upper_bound)
n = 1
while n < upper_bound:
    print n
    for r in range(1, len(str(n))):
        for idxs in combinations(range(len(str(n)) - 1), r):
            prime_family = []
            for new_digit in range(10):
                if new_digit == 0 and idxs[0] == 0:
                    continue
                x = replace_digits(n, new_digit, idxs)
                if x in primes:
                    prime_family.append(x)
            if len(prime_family) == 8:
                print prime_family
                exit()
    n += 1
