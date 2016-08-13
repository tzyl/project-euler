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

with open("p067_triangle.txt", "r") as f:
    rows = [map(int, line.split()) for line in f.read().splitlines()]

# ITERATIVE TOP DOWN SOLUTION
#
#
max_path_sum = rows[0]
# Iterate row by row keeping track of the maximum path sums up to that point.
for row in rows[1:]:
    # Create temp with the first entry (only one way to get there).
    # Fill the new maximums for the next row.
    temp = [max_path_sum[0] + row[0]]
    for i in xrange(len(max_path_sum) - 1):
        temp.append(row[i + 1] + max(max_path_sum[i], max_path_sum[i+1]))
    # Add the last entry (only one way to get there).
    temp.append(max_path_sum[-1] + row[-1])

    # Set this as the new maximum path sum row.
    max_path_sum = temp

print max(max_path_sum)

# RECURSIVE SOLUTION USING MEMOIZATION
#
#
print maximum_path_recursive(0, 0)
