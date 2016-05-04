def find_lattice_paths(n, pos):
    """
    Returns the number of lattice paths in an nxn lattice starting from the
    position tuple pos.
    """
    num_paths = 0

    if pos == (n, n):
        return 1
    else:
        x, y = pos

        if x + 1 <= n:
            num_paths += find_lattice_paths(n, (x + 1, y))

        if y + 1 <= n:
            num_paths += find_lattice_paths(n, (x, y + 1))

    return num_paths


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(40) / (factorial(20) * factorial(20))
