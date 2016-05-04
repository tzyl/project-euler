def is_permuted_multiple(x):
    "Returns true if x, 2x, 3x, 4x, 5x, 6x contain the same digits."
    digits = sorted(str(x))
    for i in range(2, 7):
        if sorted(str(i * x)) != digits:
            return False
    return True


# Note that x must begin with the digit 1 for 6x to contain the same digits.
i = 0
while True:
    x = int("1" + str(i))
    if is_permuted_multiple(x):
        print x
        break
    i += 1
