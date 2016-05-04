amount = 200
a = 200
b = 100
c = 50
d = 20
e = 10
f = 5
g = 2
h = 1


n = 0
for n_a in range(200/a + 1):
    for n_b in range(200/b + 1):
        for n_c in range(200/c + 1):
            for n_d in range(200/d + 1):
                for n_e in range(200/e + 1):
                    for n_f in range(200/f + 1):
                        for n_g in range(200/g + 1):
                                if (a*n_a + b*n_b + c*n_c + d*n_d + e*n_e +
                                        f*n_f + g*n_g <= 200):
                                    n += 1
                                    #print n_a, n_b, n_c, n_d, n_e, n_f, n_g

print n
