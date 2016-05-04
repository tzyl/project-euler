distinct_powers = set([a ** b for a in xrange(2, 101) for b in xrange(2, 101)])
print len(distinct_powers)
