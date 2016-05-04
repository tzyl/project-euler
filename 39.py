squares = set(x*x for x in xrange(500))
p_count = {}

for a in xrange(1, 500):
    b = a
    c = (a*a + b*b)**0.5
    while a + b + c <= 1000:
        if (a*a + b*b) in squares:
            p = int(c) + a + b
            p_count[p] = p_count.setdefault(p, 0) + 1
        b += 1
        c = (a*a + b*b)**0.5


print max(p_count.iteritems(), key=lambda item: item[1])
