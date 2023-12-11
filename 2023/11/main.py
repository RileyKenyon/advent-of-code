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


def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        lines = [list(line) for line in lines]
        lines = expand_array(lines)
        joint = [''.join(line) for line in lines]
        # print(joint)
        coord = []
        for idx, line in enumerate(joint):
            col = line.find('#')
            for col in [i for i,val in enumerate(line) if val == '#']:
                # Galaxy here - add coordinate
                coord.append([idx, col])
        # iterate through combinations of coordinates
        d = 0
        c = combinations(coord, 2)
        for pair in c:
            # Get distance - add to the sum
            dist = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
            d+= dist
        print(d)
if __name__ == "__main__":
    main()