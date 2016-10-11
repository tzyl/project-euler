def triangle(n):
    """Returns the nth triangle number."""
    return n * (n + 1) / 2


def count_factors(x):
    """Returns the number of factors of x."""
    count = 0
    y = 1
    while y * y < x:
        if x % y == 0:
            count += 2
        y += 1
    if y * y == x:
        count += 1
    return count


if __name__ == '__main__':
    n = 1
    while count_factors(triangle(n)) <= 500:
        n += 1
    print triangle(n)
