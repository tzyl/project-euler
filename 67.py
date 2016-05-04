with open("p067_triangle.txt", "r") as f:
    rows = [map(int, line.split()) for line in f.read().strip().split('\n')]

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
