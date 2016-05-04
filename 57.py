def root2_iteration(n):
    """
    Returns the nth iteration of the infinite fraction expansion of root two
    as a (numerator, denominator) tuple pair.
    """
    num = 0
    den = 1
    for i in range(n):
        num += 2 * den
        num, den = den, num
    num += den

    d = gcd(num, den)
    num /= d
    den /= d

    return (num, den)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


count = 0
for n in xrange(1, 1001):
    (num, den) = root2_iteration(n)
    if len(str(num)) > len(str(den)):
        count += 1
print count
