squares = set(x*x for x in xrange(1, 1000))


def continued_fraction(n):
    "Returns the period of the continued fraction representation of root n."
    if n in squares:
        return 0

    remainder = int(n ** 0.5)
    frac = ((0, 0), 1, (1, n), -remainder)
    idx = 0

    history = {}
    history[frac] = (idx, remainder)

    while True:
        idx += 1
        remainder, frac = rationalise(frac)
        # Invert fraction.
        frac = (frac[2], frac[3], frac[0], frac[1])

        if frac in history:
            first_idx = history[frac][0]
            remainders = sorted([history[f] for f in history], key=lambda x: x[0])
            remainders = [a[1] for a in remainders] + [remainder]
            print remainders[:first_idx + 1], remainders[first_idx + 1:]
            return idx - first_idx
        else:
            history[frac] = (idx, remainder)


# Fraction in the form  (a, b, c, d).
def rationalise(fraction):
    a, b, c, d = fraction
    y, z = ((0, 0), c[0]*c[0] * c[1] - d*d)
    w, x = (b*c[0], c[1]), -b*d
    w = factor_square_root(w)

    f = reduce(gcd, [w[0], x, z])
    w = (w[0]/f, w[1])
    x /= f
    z /= f

    remainder = int((w[0] * ((w[1]) ** 0.5) + x) / z)
    x -= remainder * z

    return (remainder, (w, x, y, z))


def factor_square_root((coeff, square)):
    i = 2
    factor = 4
    while factor <= square:
        if square % factor == 0:
            coeff *= i
            square /= factor
            i = 2
            factor = 4
            continue
        i += 1
        factor = i*i
    return (coeff, square)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


odd_count = 0
for n in xrange(1, 10001):
    if continued_fraction(n) % 2 == 1:
        odd_count += 1
print odd_count
