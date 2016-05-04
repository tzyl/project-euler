lst = []
for x in xrange(2, 354294):
    if sum(int(digit) ** 5 for digit in str(x)) == x:
        lst.append(x)

print sum(lst)
