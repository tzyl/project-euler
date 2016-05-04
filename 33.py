def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

digit_cancelling = []
for i in range(10, 99):
    for j in range(i + 1, 100):
        if str(i)[-1] == str(j)[0] and str(j)[-1] != "0":
            if float(i)/j == float(str(i)[0])/float(str(j)[-1]):
                digit_cancelling.append("%d/%d" % (i, j))

numerator = 1
denominator = 1
for frac in digit_cancelling:
    numerator *= int(frac[:2])
    denominator *= int(frac[-2:])

c = gcd(numerator, denominator)
while c > 1:
    numerator /= c
    denominator /= c
    c = gcd(numerator, denominator)

print "%d/%d" % (numerator, denominator)
