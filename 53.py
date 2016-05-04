def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def nCr(n, r):
    if not 0 <= r <= n:
        return
    return factorial(n) / (factorial(r) * factorial(n-r))


count = 0
for n in xrange(1, 101):
    for r in xrange(n + 1):
        if nCr(n, r) > 1000000:
            count += 1
print count
