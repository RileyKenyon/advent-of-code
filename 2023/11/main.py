import math
import sys
import os
import re
from collections import namedtuple
from functools import reduce
import copy
from itertools import combinations
def expand_array(l):
    out = copy.deepcopy(l)
    # expand row
    offset = 0
    for idx, line in enumerate(l):
        if line.count('#') == 0:
            out.insert(idx+1+offset, line)
            offset+=1
    width = len(l[0])
    # expand column
    offset = 0
    for i in range(0, width):
        if all([o[i] == '.' for o in l]):
            print(i)
            for o in out:
                o.insert(i+1+offset, '.')
            offset+=1
    return out

multiplier = 1000000 - 1
def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        coord = []
        empty_col = [True] * len(lines[0])
        empty_row = [True] * len(lines)
        for idx, line in enumerate(lines):
            for col in [i for i,val in enumerate(line) if val == '#']:
                # Galaxy here - add coordinate
                coord.append([idx, col])
                empty_row[idx] = False
                empty_col[col] = False 
            
        # iterate through combinations of coordinates
        d = 0
        c = combinations(coord, 2)
        for pair in c:
            # Get distance - add to the sum
            x1 = pair[0][0]
            y1 = pair[0][1]

            x2 = pair[1][0]
            y2 = pair[1][1]

            if x2 < x1:
                tmp = copy.deepcopy(x1)
                x1 = x2
                x2 = tmp
            if y2 < y1:
                tmp = copy.deepcopy(y1)
                y1 = y2
                y2 = tmp      
            extra = 0
            extra += empty_row[x1:x2].count(True) * multiplier
            extra += empty_col[y1:y2].count(True) * multiplier
            dist = abs(x1 - x2) + abs(y1 - y2)
            d+= dist + extra
        print(d)
if __name__ == "__main__":
    main()