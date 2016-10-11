def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == '__main__':
    result = 1
    for x in xrange(1, 21):
        result = lcm(result, x)
    print result
