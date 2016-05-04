def concat_product(x, n):
    "Returns the concatenated product of integer x with (1, 2, ..., n)."
    s = ""
    for i in range(1, n + 1):
        s += str(i * x)
    return int(s)


def is_pandigital(x):
    "Returns true if the number x is 1 to 9 pandigital."
    s = str(x)
    if len(s) != 9:
        return False

    digit_set = set(int(char) for char in s)
    for i in range(1, 10):
        if i not in digit_set:
            return False

    return True


# Lower bound x = 1, n = 9. This is the largest possible value of n.
largest_pandigital = 123456789
n = 2
while n < 9:
    x = 1
    y = concat_product(x, n)
    while y < 1000000000:
        if is_pandigital(y) and y > largest_pandigital:
            largest_pandigital = y
        x += 1
        y = concat_product(x, n)
    n += 1

print largest_pandigital
