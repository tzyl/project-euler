prev_prev = 1
prev = 1
current = prev_prev + prev
n = 3

while len(str(current)) < 1000:
    n += 1
    prev_prev, prev = prev, current
    current = prev_prev + prev

print n
