def d(n):
    "Returns the sum of proper divisors of n."
    proper_divisors = []
    for x in xrange(1, n):
        if n % x == 0:
            proper_divisors.append(x)
    return sum(proper_divisors)

amicable_numbers = []
for a in xrange(2, 10000):
    if a not in amicable_numbers:
        b = d(a)
        if d(b) == a and a != b:
            amicable_numbers.append(a)
            if b < 10000:
                amicable_numbers.append(b)

print sum(amicable_numbers)
