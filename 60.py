from itertools import combinations


def find_lower_concatenating_primes(x, lst):
    "Returns a list of smaller primes that double concatenate to a prime."
    concatenating = []
    for prime in lst:
        if prime >= x:
            return concatenating
        elif double_concatenate_prime(prime, x):
            concatenating.append(prime)


def double_concatenate_prime(x, y):
    left = concatenate(x, y)
    right = concatenate(y, x)
    if left in prime_set and right in prime_set:
        return True
    elif not is_prime(left) or not is_prime(right):
        return False
    return True


def concatenate(x, y):
    return int(str(x) + str(y))


def intersect(a, b):
    return list(set(a) & set(b))


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

    return primes


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

prime_list = prime_sieve(100000000)
prime_set = set(prime_list)

"""
for top in prime_list:
    print top
    concatenating4 = find_lower_concatenating_primes(top, prime_list)
    for a in concatenating4:
        concatenating3 = find_lower_concatenating_primes(a, concatenating4)
        for b in concatenating3:
            concatenating2 = find_lower_concatenating_primes(b, concatenating3)
            for c in concatenating2:
                concatenating1 = find_lower_concatenating_primes(c, concatenating2)
                for d in concatenating1:
                    print d, c, b, a, top
                    print sum([d, c, b, a, top])
                    exit()

"""

for i, top in enumerate(prime_list):
    print i, top
    concatenating = [p for p in prime_list[:i] if double_concatenate_prime(p, top)]

    if len(concatenating) < 4:
        continue

    for c in combinations(concatenating, 4):
        set_of_five = [top] + list(c)
        for x, y in combinations(set_of_five, 2):
            skip = False
            if not double_concatenate_prime(x, y):
                skip = True
                break

        if skip:
            continue

        print set_of_five, sum(set_of_five)
        exit()
