import sys
import numpy as np

# Global grid
grid = np.array([])
truth_grid = np.array([])
w = 0
h = 0
path = []
included_paths = []

def in_bounds(i,j):
     return True if 0 <= i < h and 0<= j < w else False

def traverse_path(point):
    global path
    row = point[0]
    col = point[1]
    idx = [[row-1, col],[row+1,col],[row,col-1],[row,col+1]]
    if truth_grid[row,col] == 1:
        for i, j in idx:
            if in_bounds(i,j):
                if truth_grid[i,j] == 1 and [i,j] not in path:
                    path.append([i,j])
                    traverse_path([i,j])


def check_neighbors(point):
    # index of nearest neighbors
    global path, truth_grid, cum_sum
    row = point[0]
    col = point[1]
    idx = [[row-1, col],[row+1,col],[row,col-1],[row,col+1]]
    if in_bounds(row,col):
        val = grid[row,col]
    else:
        return

    # recursively call function until lowest point is reached or current value is a 9
    if (val!= 9):
        for i, j in idx:
            if in_bounds(i,j):
                next_val = grid[i,j]
                if next_val !=9:
                    truth_grid[i,j] = 1
                    if next_val < val:
                        check_neighbors([i,j])
    return

def main():
    """
    --- Day 9: Smoke Basin ---
    Lava tubes - map how smoke moves
    1.) look for the lowest points in the grid, diagonals do not count
        risk level is 1 plus its height
        sum the risk of all low points on the heightmap
    2.) Get the size of basins - number of locations within the basin including the lowest point
        locations with height of 9 do not count as being in any basin
        Locations can only be part of exactly one basin
    """
    total_risk = 0
    max_sum = [0]

    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Split lines, convert into 2D array
        raw_lines = f.read().splitlines()

        # global grid
        global grid, w, h, truth_grid
        grid = [[int(val) for val in ' '.join(line).split()] for line in raw_lines]
        grid = np.array(grid)
        truth_grid = np.zeros_like(grid)
        h = np.size(grid, axis=0)
        w = np.size(grid, axis=1)

        # Loop through grid
        for row in range(0,h):
            for col in range(0,w):
                check_neighbors([row,col])

        # traverse truth grid to get sum
        global path, included_paths
        path_size = []
        for row in range(0,h):
            for col in range(0,w):
                if ([row,col]) not in included_paths:
                    traverse_path([row,col])
                    path_size.append(len(path))
                    for p in path:
                        included_paths.append(p)
                    path = []
        max_basins = sorted(path_size)[-3:]
        print(max_basins)
        print(max_basins[0] * max_basins[1] * max_basins[2])
                

if __name__ == "__main__":
    main()