largest_collatz = (0, 0)

for x in xrange(1, 1000000):
    collatz_len = 1
    term = x

    while term != 1:
        if term % 2 == 0:
            term /= 2
        else:
            term = 3*term + 1
        collatz_len += 1

    if collatz_len > largest_collatz[1]:
        largest_collatz = (x, collatz_len)

print largest_collatz
