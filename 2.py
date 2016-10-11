a, b = 1, 2
result = 0
while a < 4000000:
    if a % 2 == 0:
        result += a
    a, b = b, a + b
print result
