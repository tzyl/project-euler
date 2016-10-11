def digit_sum(n):
    """Returns the sum of the digits of the integer n."""
    return sum(map(int, list(str(n))))

print reduce(lambda x, y: x if x > y else y,
             [digit_sum(a ** b) for a in range(100) for b in range(100)])
