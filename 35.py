def is_prime(n):
    "Returns True if integer n is prime and False if not."
    if n < 2:
        return False
    elif 2 <= n <= 3:
        return True

    for x in xrange(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True


def digit_rotations(n):
    "Returns a list of digit rotations of the integer n."
    digit_rotations = []
    i = 0
    str_n = str(n)
    while i < len(str_n):
        if n not in digit_rotations:
            digit_rotations.append(n)
        str_n = str_n[1:] + str_n[0]
        n = int(str_n)
        i += 1
    return digit_rotations


def is_circular_prime(n):
    "Returns True if all rotations of the digits of n are prime."
    for x in digit_rotations(n):
        if not is_prime(x):
            return False
    return True


circular_primes = []
for n in xrange(1000000):
    if is_circular_prime(n):
        circular_primes.append(n)

print len(circular_primes)
