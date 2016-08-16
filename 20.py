from resources import prime_factorisation


# Recursive factorial.
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Iterative factorial.
def factorial(n):
    if n == 0:
        return 1
    prod = 1
    for i in xrange(1, n + 1):
        prod *= i
    return prod


# Brute force works in python due to automatic big number type.
digits = [int(c) for c in str(factorial(100))]
# print factorial(100)
print sum(digits)


# Solution not relying on big number type using prime factorisation:
def tidy_coeffs(power_10_coeffs):
    # Tidies all coefficients to be between 0-9.
    for power_10 in sorted(power_10_coeffs):
        if power_10_coeffs[power_10] >= 10:
            power_10_coeffs[power_10 + 1] = power_10_coeffs.setdefault(power_10 + 1, 0) + power_10_coeffs[power_10] / 10
            power_10_coeffs[power_10] %= 10


def factorial_digit_sum(n):
    # Returns the digit sum of factorial(n).
    prime_factor_count = {}
    for i in xrange(1, n + 1):
        prime_factors = prime_factorisation(i)
        for prime_factor in prime_factors:
            prime_factor_count[prime_factor] = prime_factor_count.setdefault(prime_factor, 0) + 1

    power_10_coeffs = {0: 1}
    for prime_factor in prime_factor_count:
        new_power_10_coeffs = {}
        contribution = prime_factor ** prime_factor_count[prime_factor]
        power_10 = 0
        while contribution:
            digit = contribution % 10

            for coeff in power_10_coeffs:
                new_power_10_coeffs[coeff + power_10] = new_power_10_coeffs.setdefault(coeff + power_10, 0) + power_10_coeffs[coeff] * digit

            contribution /= 10
            power_10 += 1

        tidy_coeffs(new_power_10_coeffs)
        power_10_coeffs = new_power_10_coeffs

    # Print the factorial as a string
    # print "".join([str(power_10_coeffs[power]) for power in sorted(power_10_coeffs, reverse=True)])

    return sum(power_10_coeffs.itervalues())

print factorial_digit_sum(100)
