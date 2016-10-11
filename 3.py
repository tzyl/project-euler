def largest_prime_factor(x):
    """Returns the largest prime factor of x."""
    if x < 2:
        return None
    largest = 1
    while x > 1:
        largest += 1
        if is_prime(largest):
            while x % largest == 0:
                x /= largest
    return largest


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


if __name__ == '__main__':
    print largest_prime_factor(600851475143)
