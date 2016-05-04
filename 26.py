def find_recpirocal_cycle_length(n):
    "Finds the length of the recurring cycle of the reciprocal 1/n."
    # Initialise dictionary to remember remainders and when they occurred.
    remainders = {}
    index = 0
    dividend = 1
    while True:
        if n > dividend:
            index += 1
            dividend *= 10
        else:
            remainder = dividend % n
            if remainder == 0:
                return 0
            elif remainder in remainders:
                return index - remainders[remainder]
            else:
                remainders[remainder] = index
                dividend = remainder

print max([(find_recpirocal_cycle_length(i), i) for i in xrange(1, 1000)])
