import math
import sys
import os
import re
from collections import namedtuple
from functools import reduce
import copy

# Left, Right, Up, Down ( X are 7)
compatible = {
    'F' : [[], ['J', 'X', '-'], [], ['J', 'L','|']],
    'J' : [['F', 'L', '-'], [], ['|', 'F', 'X'], []],
    'X' : [['F', 'L', '-'], [], [], ['|', 'J', 'L']],
    'L' : [[], ['J', 'X', '-'], ['|', 'F', 'X'], []],
    '|' : [[], [], ['F', 'X','|'], ['J', 'L', '|']],
    '-' : [['F', 'L','-'], ['J', 'X', '-'], [], []],
    'S' : [['F', 'L', '-'],['J', 'X', '-'], ['F','X','|'],['J','L','|']]
}

def get_neighbors(map, start, width):
    n = []
    checks = [start - 1, start + 1, start - width, start + width]
    for idx in checks:
        if idx >= 0 and idx < len(map):
            # valid index
            n.append(map[idx] if map[idx] != '\n' else [])
        else:
            n.append([])
    return n

def update_map(map, start, width, value):
    neighbors = get_neighbors(map,start, width)
    c = copy.copy(map)
    # print(neighbors, compatible[map[start]])
    for idx, [p, comp] in enumerate(zip(neighbors, compatible[c[start]])):
        if p != [] and p in comp:
            # print(p)
            c[start] = value
            checks = [start - 1, start + 1, start - width, start + width]
            return update_map(c, checks[idx], width, str(int(value) + 1))
    return c

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        pipe = f.read()
        pipe = re.sub('7', 'X', pipe)
        # print(pipe)
        m = [0] * len(pipe)
        width = len(pipe.split('\n')[0])
        pipe = ''.join(pipe.splitlines())
        start = re.search('S', pipe).start()
        # determine starting pipe type
        pipe = list(pipe)
        neighbors = get_neighbors(pipe, start, width)
        maps = []
        for idx, [p, comp] in enumerate(zip(neighbors, compatible[pipe[start]])):
            if p != [] and p in comp:
                pipe[start] = '0'
                checks = [start - 1, start + 1, start - width, start + width]
                # print("Start: ", pipe[checks[idx]])
                m = update_map(pipe, checks[idx], width, '1')
                # print(m)
                maps.append(m)
        out = []
        for i in range(0, len(pipe)):
            # print([map[i] for map in maps])
            out.append(min([int(map[i]) if map[i].isdigit() else 0 for map in maps]))
        print(max(out))



if __name__ == "__main__":
    main()