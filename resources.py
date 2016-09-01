import functools


def memoize(fn):
    # Acts as a cache to remember previously calculated function values.
    cache = {}

    # Use functools.wraps to preserve the original function's metadata.
    @functools.wraps(fn)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return memoizer


def prime_sieve(n):
    "Returns a set of all primes <= n."
    primes = []
    a = [True] * (n + 1)
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes.append(i)
            for j in xrange(i, n + 1, i):
                a[j] = False

    return set(primes)


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


# def permutations(lst):
#     """
#     SLOWER
#     Returns all permutations of obj in a list.
#     """
#     if len(lst) <= 1:
#         return [lst]

#     p = []

#     # for i, elt in enumerate(lst):
#     #     p.extend([elt + perm for perm in permutations(lst[:i] + lst[i+1:])])

#     for i in range(len(lst)):
#         for perm in permutations(lst[:i] + lst[i+1:]):
#             p.append(lst[i:i+1] + perm)

#     return p


def permutations(obj):
    """
    Returns all permutations of obj in a list.
    """
    if len(obj) <= 1:
        return [obj]

    p = []

    for perm in permutations(obj[1:]):
        # print perm
        for i in range(len(obj)):
            # print perm[:i], obj[0:1], perm[i:]
            p.append(perm[:i] + obj[0:1] + perm[i:])

    return p


def permutations_generator(obj):
    """
    Yields all permutations of obj.
    """
    if len(obj) <= 1:
        yield obj
    else:
        for perm in permutations(obj[1:]):
            # print perm
            for i in range(len(obj)):
                # print perm[:i], obj[0:1], perm[i:]
                yield perm[:i] + obj[0:1] + perm[i:]


def combinations(lst, r):
    "Returns all combinations of size r from a list as a list of sets."
    n = len(lst)
    if r > n:
        return
    elif r == 1:
        return [set([elt]) for elt in lst]
    elif r == n:
        return [set(lst)]
    else:
        return (combinations(lst[1:], r) +
                [set([lst[0]]).union(c) for c in combinations(lst[1:], r - 1)])


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def nCr(n, r):
    if not 0 <= r <= n:
        return
    return factorial(n) / (factorial(r) * factorial(n-r))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
