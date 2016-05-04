def is_cyclic(ordered_set):
    "Returns true if the ordered set is cyclic."
    str_list = [str(x) for x in ordered_set]
    l = len(str_list)
    for i in range(l):
        if str_list[i][-2:] != str_list[(i+1) % l][:2]:
            return False
    return True


def find_cyclical_set(current_set, needed):
    if len(current_set) == 5:
        last = current_set[-1]
        first = current_set[0]
        need = int(str(last)[-2:] + str(first)[:2])

        if need in needed[0]:
            cyclical_set = current_set + [need]
            #print cyclical_set, sum(cyclical_set)
            return cyclical_set, sum(cyclical_set)
        else:
            return None
    elif len(current_set) == 0:
        for x in needed[0]:
            cyclical_set = find_cyclical_set([x], needed[1:])
            if cyclical_set is not None:
                return cyclical_set
        return None
    else:
        last = current_set[-1]
        for i, polygon_list in enumerate(needed):
            candidates = [x for x in polygon_list if str(last)[-2:] == str(x)[:2]]
            if not candidates:
                continue

            new_needed = list(needed)
            new_needed.pop(i)
            for c in candidates:
                new_set = current_set + [c]
                cyclical_set = find_cyclical_set(new_set, new_needed)
                if cyclical_set is not None:
                    return cyclical_set
        return None


def triangle(n):
    return n*(n+1)/2


def square(n):
    return n*n


def pentagon(n):
    return n*(3*n-1)/2


def hexagon(n):
    return n*(2*n-1)


def heptagon(n):
    return n*(5*n-3)/2


def octagon(n):
    return n*(3*n-2)


triangles = [triangle(n) for n in xrange(200) if len(str(triangle(n))) == 4]
squares = [square(n) for n in xrange(200) if len(str(square(n))) == 4]
pentagons = [pentagon(n) for n in xrange(200) if len(str(pentagon(n))) == 4]
hexagons = [hexagon(n) for n in xrange(200) if len(str(hexagon(n))) == 4]
heptagons = [heptagon(n) for n in xrange(200) if len(str(heptagon(n))) == 4]
octagons = [octagon(n) for n in xrange(200) if len(str(octagon(n))) == 4]

needed = [triangles, squares, pentagons, hexagons, heptagons, octagons]
cyclical_set = find_cyclical_set([], needed)
if cyclical_set is not None:
    print cyclical_set


"""
for a in triangles:
    set_of_six = [a]
    needed = [squares, pentagons, hexagons, heptagons, octagons]
    for i, polygon_list in enumerate(needed):
        copy = list(needed)
        x = copy.pop(i)
        candidates = [y for y in x if str(a)[-2:] == str(y)[:2]]
        for b in candidates:
            set_of_six.append(b)
"""

"""
for a in triangles:
    for b in squares:
        for c in pentagons:
            for d in hexagons:
                for e in heptagons:
                    for f in octagons:
                        print a, b, c, d, e, f
                        for perm in permutations((a, b, c, d, e, f)):
                            if is_cyclic(perm):
                                print perm
                                exit()
"""
