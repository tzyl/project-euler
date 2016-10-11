def find_permutations(lst):
    """Returns all permutations in a list of the string elements in lst."""
    if len(lst) <= 1:
        return lst

    permutations = []
    for elt in lst:
        reduced_list = list(lst)
        reduced_list.pop(lst.index(elt))
        permutations.extend([elt + perm for perm in
                             find_permutations(reduced_list)])
    return permutations

perm_lst = find_permutations([str(num) for num in range(10)])
perm_lst.sort()
print perm_lst[999999]
