def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

digits = [int(c) for c in str(factorial(100))]
print sum(digits)
