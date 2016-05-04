i = 286
j = 165
k = 143

t = i*(i + 1)/2
p = j*(3*j - 1)/2
h = k*(2*k - 1)
while True:
    while p < t:
        j += 1
        p = j*(3*j - 1)/2
    while h < t:
        k += 1
        h = k*(2*k - 1)

    if t == p and t == h:
        print p
        break

    i += 1
    t = i*(i + 1)/2
