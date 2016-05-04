def is_abundant(n):
    "Returns true if natural number n is abundant."
    if n < 12:
        return False

    factors = [1]
    for x in xrange(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x ** 2 == n:
                factors.append(x)
            else:
                factors.append(x)
                factors.append(n / x)

    return sum(factors) > n

abundant_numbers = [x for x in xrange(28123) if is_abundant(x)]

sum_of_two_abundant = set([x + y for x in abundant_numbers
                           for y in abundant_numbers if x + y < 28123])

print sum(filter(lambda x: x not in sum_of_two_abundant, xrange(28123)))
