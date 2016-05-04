from itertools import permutations


def digit_permutations(n):
    "Returns a set of the permutations of the digits of n."
    return set(int("".join(p)) for p in permutations(str(n)) if p[0] != "0")


def is_permutation(x, y):
    "Returns True if integers x and y are permutations of each other."
    return sorted(str(x)) == sorted(str(y))


# This attempt isn't good enough
"""
def find_cubic_permutations(count):
    "Returns the smallest cube such that exactly count permutations are cubes."
    cubes = [x*x*x for x in xrange(10000)]
    search_cubes(cubes)
"""

"""
cubes = [x*x*x for x in xrange(10000)]
cubes_set = set(cubes)
for i, x in enumerate(cubes):
    print i, x

    count = 0
    for digit_p in digit_permutations(x):
        if digit_p in cubes_set:
            count += 1

    if count == 5:
        print x
        break
"""

# This works but is a bit slow.
"""
cube_permutations = {}
n = 1
while True:
    cube = n*n*n
    l = len(str(cube))
    print n, cube
    if l not in cube_permutations:
        cube_permutations[l] = []

    found_perm = False
    for perm_group in cube_permutations[l]:
        if is_permutation(perm_group[0], cube):
            found_perm = True
            perm_group.append(cube)
            print perm_group
            if len(perm_group) == 5:
                print perm_group
                exit()
            break

    if not found_perm:
        cube_permutations[l].append([cube])

    n += 1
"""

# This is a much faster solution.
cube_permutations = {}
n = 1
while True:
    cube = n*n*n
    min_perm = "".join(sorted(list(str(cube))))
    cube_permutations.setdefault(min_perm, []).append(cube)
    if len(cube_permutations[min_perm]) == 5:
        print cube_permutations[min_perm][0], cube_permutations[min_perm]
        break
    n += 1
