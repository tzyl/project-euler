def sum_number_spiral_diagonals(n):
    "Returns the sum of the diagonals on an nxn number spiral (n must be odd)."
    if n % 2 == 0:
        print "n must be odd."
        return
    else:
        current_n = 1
        sum_diagonals = 1
        num = 1
        while current_n < n:
            for i in xrange(4):
                num += current_n + 1
                sum_diagonals += num
            current_n += 2
        return sum_diagonals

print sum_number_spiral_diagonals(1001)
