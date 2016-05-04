def permutations(lst):
    if len(lst) == 1:
        return lst

    p = []
    for elt in lst:
        reduced_list = list(lst)
        reduced_list.pop(lst.index(elt))
        p.extend([elt + perm for perm in permutations(reduced_list)])
    return p

# First create all permutations of 123456789.
p = permutations([str(i) for i in range(1, 10)])
pandigital = []
for perm in p:
    for i in range(1, 8):
        for j in range(1, 9 - i):
            if int(perm[:i]) * int(perm[i:i+j]) == int(perm[i+j:]):
                pandigital.append(int(perm[i+j:]))

print sum(set(pandigital))
