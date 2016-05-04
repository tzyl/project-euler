def convergent_of_e(n):
    """
    Returns (numerator, denominator) of the nth convergent of the continued
    fraction of e.
    """
    if n == 1:
        return 2

    # Coefficients of the continued fraction.
    coeffs = [1] * (n - 1)

    idx = 1
    i = 1
    while idx < n - 1:
        coeffs[idx] = 2*i
        i += 1
        idx += 3

    num = 0
    den = 1
    for c in coeffs[::-1]:
        num += c * den
        num, den = den, num

    # Add the starting 2.
    num += 2 * den

    d = gcd(num, den)
    num /= d
    den /= d

    return (num, den)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sum_digits(n):
    return sum(int(c) for c in str(n))


print sum_digits(convergent_of_e(100)[0])
