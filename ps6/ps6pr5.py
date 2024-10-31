#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

def row_index_grid(num_rows, num_cols):
    """ returns a new grid that has its values as its row num"""
    grid = create_grid(num_rows, num_cols)
    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = r
    return grid

def num_between(grid, n1, n2):
    """ returns number of values in grid between n1 and n2"""
    num = 0
    for i in grid:
        for j in i:
            if n1 <= j <= n2:
                num += 1
    return num

def copy(grid):
    """ returns a deep copy of a grid """
    num_rows = len(grid)
    num_cols = len(grid[0])
    new_grid = create_grid(num_rows, num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            new_grid[i][j] = grid[i][j]
    return new_grid

def double_with_cap(grid, cap):
    """ doubles every value in a grid up until a cap """
    num_rows = len(grid)
    num_cols = len(grid[0])
    for i in range(num_rows):
        for j in range(num_cols):
            new = grid[i][j] * 2
            if new > cap:
                grid[i][j] = cap
            else:
                grid[i][j] = new

def sum_evens_in_col(grid, colnum):
    """ sums all the eve numbers in a column """ 
    sum = 0
    num_rows = len(grid)
    for r in range(num_rows):
        if grid[r][colnum] % 2 == 0:
            sum += grid[r][colnum]
    return sum
