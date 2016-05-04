def d(n):
    "Returns the nth digit of the concatenation of the positive integers."
    string = "".join([str(x) for x in xrange(1, 1000001)])
    return int(string[n - 1])

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
