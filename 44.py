"""
def p(n):
    "Returns the nth pentagonal number."
    return n*(3*n - 1)/2

pentagons = [p(n) for n in xrange(1, 4000)]
pentagon_set = set(pentagons)
D = []
for i, p_j in enumerate(pentagons[:-1]):
    for p_k in pentagons[i+1:]:
        if p_k - p_j in pentagon_set and p_k + p_j in pentagon_set:
            print p_k, p_j
            D.append(p_k - p_j)

print D
"""

penta = set()
x = 0
while True:
    x += 1
    p = (x*(3*x-1))/2
    penta.add(p)
    for y in penta:
        if p-y in penta and p-2*y in penta:
            print p-2*y
            exit()
