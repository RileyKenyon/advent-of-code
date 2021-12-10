import sys
import numpy as np
import copy

def main():
    """
    --- Day 5: Hydrothernal venture ---
    x1,ya -> x2,y2
    0,9 -> 5,9
    8,0 -> 0,8
    9,4 -> 3,4
    2,2 -> 2,1
    7,0 -> 7,4
    6,4 -> 2,0
    0,9 -> 2,9
    3,4 -> 1,4
    0,0 -> 8,8
    5,5 -> 8,2

    Part #1: Only consider horizontal and vertical lines
    x1 = x2 or y1 = y2
    e.g.
    0,0 is top left
    9,9 is bottom right

    Determine the number of points that have at least two lines overlap
    """
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        [point_list_start, point_list_end, width, height] = parse_lines(lines)
        grid = update_grid(point_list_start, point_list_end, width, height)
        num_overlap = get_overlap_sum(grid, 2)
        print(num_overlap)

def parse_lines(lines):
    # data is non-zero, can just look for the max, and min for width and height
    x_max = 0
    y_max = 0
    start_list = []
    end_list = []
    for line in lines:
        coord = line.split(' -> ')
        [x1,y1] = coord[0].split(',')
        [x2,y2] = coord[1].split(',')
        x_local_max = max(int(x1),int(x2)) + 1
        y_local_max = max(int(y1), int(y2)) + 1
        x_max = x_local_max if x_local_max > x_max else x_max
        y_max = y_local_max if y_local_max > y_max else y_max
        start_list.append([int(x1), int(y1)])
        end_list.append([int(x2), int(y2)])
    return start_list, end_list, x_max, y_max

def update_grid(start, end, width, height):
    # allocate grid
    grid = np.zeros([width, height])
    # Start and end are the same length
    for i in range(0, len(start)):
        # allocate coordinates
        x1 = start[i][0]
        y1 = start[i][1]
        x2 = end[i][0]
        y2 = end[i][1]

        # Vertical lines
        # End point is not inclusive - need to add 1
        if x1 == x2:
            grid[x1,min(y1,y2):max(y1,y2) + 1] += 1

        # Horizontal lines
        elif y1 == y2:
            grid[min(x1,x2):max(x1,x2) + 1, y1] += 1
    return grid
    
def get_overlap_sum(grid, min_overlap):
    return sum(sum(grid >= min_overlap))


if __name__ == "__main__":
    main()