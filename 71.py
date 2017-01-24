def ordered_fractions(numerator, denominator, d):
    """Finds the numerator of the fraction immediately to the left of the
    fracton given by numerator, denominator in the ordered list of proper
    fractions with denominator at most d.
    """
    best_numerator = 0
    best_denominator = 1
    for candidate_denominator in xrange(1, d + 1):
        candidate_numerator = (numerator * candidate_denominator - 1) / denominator
        if candidate_numerator * best_denominator > best_numerator * candidate_denominator:
            best_numerator = candidate_numerator
            best_denominator = candidate_denominator
    c = gcd(best_numerator, best_denominator)
    return best_numerator / c, best_denominator / c


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    print ordered_fractions(3, 7, 1000000)
