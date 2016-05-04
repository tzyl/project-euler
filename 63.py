n = 1
count = 0
while True:
    current_count = 0
    for x in xrange(1, 10):
        if len(str(x ** n)) == n:
            current_count += 1
    if current_count == 0:
        break
    count += current_count
    n += 1
print count
