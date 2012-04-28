from fp_util import *

def compute_score(grid):
    return 5

grid = []

def swap_horiz(i, j):
    tmp = grid[i][j]
    grid[i][j] = grid[i][j+1]
    grid[i][j+1] = tmp

def swap_vert(i, j):
    tmp = grid[i][j]
    grid[i][j] = grid[i+1][j]
    grid[i+1][j] = tmp

def solve(x, y, case):
    max_score = 0
    # try horizontal swaps
    for i in xrange(x):
        for j in xrange(y-1):
            swap_horiz(i, j)
            new_score = compute_score(grid)
            swap_horiz(i, j)
            if new_score > max_score:
                max_score = new_score
    # try vertical swaps
    for i in xrange(x-1):
        for j in xrange(y):
            swap_vert(i, j)
            new_score = compute_score(grid)
            swap_vert(i, j)
            if new_score > max_score:
                max_score = new_score
    print "Case #{0}: {1}".format(case, max_score)
    

if __name__ == '__main__':
    test_cases = read_int()
    for i in xrange(test_cases):
        x, y = read_list(int, False)
        grid = []
        for rows in xrange(x):
            grid.append(read_list(None, False, True))
        # print grid
        solve(x, y, i)
