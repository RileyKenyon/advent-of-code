import sys
import numpy as np

def main():
    """
    --- Day 9: Smoke Basin ---
    Lava tubes - map how smoke moves
    1.) look for the lowest points in the grid, diagonals do not count
        risk level is 1 plus its height
        sum the risk of all low points on the heightmap
    """
    total_risk = 0
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Split lines, convert into 2D array
        raw_lines = f.read().splitlines()
        grid = [[int(val) for val in ' '.join(line).split()] for line in raw_lines]
        grid = np.array(grid)
        h = np.size(grid, axis=0)
        w = np.size(grid, axis=1)

        # Loop through grid
        for row in range(0,h):
            for col in range(0,w):
                # create indexes to get values
                l = []
                idx = [[row-1, col],[row+1,col],[row,col-1],[row,col+1]]
                for i, j in idx:
                    if 0 <= i < h and 0<= j < w:
                        l.append(grid[i,j])
                
                # current value - see if less than all others
                val = grid[row,col]
                if val < min(l):
                    total_risk += val + 1
        print(total_risk)

if __name__ == "__main__":
    main()