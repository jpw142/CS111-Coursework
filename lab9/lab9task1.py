#
# lab9task1.py (Lab 9, Task 1)
#
# Debugging a function that processes a 2-D list
#
# Computer Science 111
#

def find_max_val(grid):
    max_val = grid[0][0]
    max_row = 0
    max_col = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if max_val < grid[r][c]:
                max_val = grid[r][c]
                max_row = r
                max_col = c

    return [max_row, max_col]
print(find_max_val([[10, 5, 8], [2, 14, 20]]))
