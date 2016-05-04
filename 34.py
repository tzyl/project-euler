def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


factorial_cache = {i: factorial(i) for i in range(10)}


def get_factorial(n):
    return factorial_cache[n]


def digits(n):
    while n:
        yield n % 10
        n /= 10


def factorial_digit_sum(n):
    return sum(map(get_factorial, digits(n)))


# First find an upper bound for digit factorials.
max_length = 1
while len(str(factorial(9) * max_length)) > max_length:
    max_length += 1

print sum(n for n in xrange(10, factorial(9) * max_length)
          if n == factorial_digit_sum(n))
