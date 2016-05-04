import itertools


pandigitals = ["".join(perm) for perm in itertools.permutations("0123456789")]
primes = [2, 3, 5, 7, 11, 13, 17]
has_property = []

for pandigital in pandigitals:
    for i in range(7):
        if int(pandigital[i+1:i+4]) % primes[i] != 0:
            break
        if i == 6:
            has_property.append(int(pandigital))

print sum(has_property)
