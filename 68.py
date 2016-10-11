from itertools import permutations


def find_soln():
    soln_set = []
    current_soln = []
    left = range(1, 11)
    find_soln2(soln_set, current_soln, left)
    return soln_set


def find_soln2(soln_set, current_soln, left):
    if not current_soln:
        for triple in permutations(left, 3):
            copy = list(left)
            copy.remove(triple[0])
            copy.remove(triple[1])
            copy.remove(triple[2])
            current_soln = [triple]
            find_soln2(soln_set, current_soln, copy)

    elif len(current_soln) == 4:
        # Fill in last step and check if this is a solution.
        x = left[0]
        y = current_soln[-1][-1]
        z = current_soln[0][1]
        current_soln.append((x, y, z))
        if check_magic_5gon(current_soln):
            soln_set.append(current_soln)

    else:
        triple_sum = sum(current_soln[-1])
        y = current_soln[-1][-1]
        for x in left:
            z = triple_sum - y - x
            if z != x and z in left:
                copy = list(left)
                copy.remove(x)
                copy.remove(z)
                soln_copy = list(current_soln)
                soln_copy.append((x, y, z))
                find_soln2(soln_set, soln_copy, copy)


def check_magic_5gon(soln):
    """
    Checks if the soln (list of 5 triples) represents a valid magic 5-gon.
    """
    for i in range(len(soln)):
        if sum(soln[i]) != sum(soln[(i+1) % len(soln)]):
            return False
    return True


def rotate(soln):
    """Rotates solution to have minimal external number first."""
    min_external_idx = soln.index(min(soln, key=lambda triple: triple[0]))
    return tuple(soln[min_external_idx:] + soln[:min_external_idx])

soln_set = find_soln()
# Remove repeats.
soln_set = list(set([rotate(soln) for soln in soln_set]))

# Create the concatenated digit strings and filter out the highest one with
# length 16.
digit_strings = ["".join(reduce(lambda x, y: x + y,
                                [map(str, triple) for triple in soln])) for
                 soln in soln_set]
digit_strings = [s for s in digit_strings if len(s) == 16]
print max(map(int, digit_strings))
