import sys
import numpy as np

energy_grid = []

def in_bounds(i, j, w, h):
    return True if 0<= i < w and 0<= j < h else False

def recursive_update(coord):
    global energy_grid

    # grid dimensions
    w = len(energy_grid[0])
    h = len(energy_grid)
    row = coord[0]
    col = coord[1]

    # initial value
    counter = 0
    
    # Increment and call recursively
    if (energy_grid[row][col] > 9):
        energy_grid[row][col] = 0
        counter+=1

        for i in [row-1,row,row+1]:
            for j in [col-1,col,col+1]:
                if in_bounds(i,j,w,h):
                    if energy_grid[i][j] != 0:
                        energy_grid[i][j]+=1
                        count = recursive_update([i,j])
                        counter+=count
    return counter

def main():
    """
    --- Day 11: Dumbo Octopus ---
    100 octopuses arranged in a 10x10 grid
    Each gains energy over time and flashes brightly when full
    Predict when the flashes of light will happen:
        - Energy Value is [0-9]
        - Each step, energy increases by 1
        - Any level > 9 flashes
        - Increases energy level of adjacent octopus by 1, INCLUDING diagonal
        - Recursive process as long as new octopus keep having their energy level > 9
        - Octopus can only flash once per step
        - Any octopus that did flash has its energy level set to 0 
    1.) Simulate 100 steps - how many total flashes are there after 100 steps
    2.) 
    """
    global energy_grid
    counter = 0
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # raw_lines = f.read().splitlines()
        lines = [map(int, line.split()) for line in " ".join(f.read()).splitlines()]
        energy_grid = [list(line) for line in lines]

        # Loop through time
        ts = 0
        while(True):
            # print(np.array(energy_grid))
            # update grid by one
            for row in range(0,len(energy_grid)):
                for col in range(0,len(energy_grid[0])):
                    energy_grid[row][col]+=1
            # process grid
            for row in range(0,len(energy_grid)):
                for col in range(0,len(energy_grid[0])):
                    # Recursively update surroundings
                    count = recursive_update([row,col])
                    counter += count
            ts+=1
            if energy_grid == [[0 for i in range(0,len(energy_grid))] for j in range(0,len(energy_grid))]:
                break
        print(ts)

            

if __name__ == "__main__":
    main()