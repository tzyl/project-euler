import resources


@resources.memoize
def maximum_path_recursive(i, j):
    """
    Returns the maximum path sum from the ith row and jth element in the row.
    """
    current = rows[i][j]
    if i == len(rows) - 1:
        return current
    max_left = maximum_path_recursive(i + 1, j)
    max_right = maximum_path_recursive(i + 1, j + 1)
    return current + max(max_left, max_right)

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

rows = [map(int, row.split()) for row in triangle.splitlines()]

# BRUTE FORCE CHECK ALL ROUTES ITERATIVE
#
#
depth = 1
routes = [(0, 75)]

while depth < len(rows):
    new_routes = []
    for index, path_sum in routes:
        new_routes.append((index, path_sum + int(rows[depth][index])))
        new_routes.append((index + 1, path_sum + int(rows[depth][index + 1])))
    routes = new_routes
    depth += 1

print max(path_sum for i, path_sum in routes)

# RECURSIVE SOLUTION USING MEMOIZATION
#
#
print maximum_path_recursive(0, 0)
