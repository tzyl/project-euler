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


def quadratic(a, b, n):
    return n**2 + a*n + b

max_consecutive_primes = 0
max_a = None
max_b = None

for a in xrange(-999, 1000):
    for b in xrange(1000):
        consecutive_primes = 0
        n = 0
        while True:
            if is_prime(quadratic(a, b, n)):
                consecutive_primes += 1
                n += 1
            else:
                break
        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            max_a = a
            max_b = b

print max_a * max_b
