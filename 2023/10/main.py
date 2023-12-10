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
    'S' : [['F', 'L', '-'],['J', 'X', '-'], ['F','X','|'],['J','L','|']],
    '.' : [[],[],[],[]]
}

def get_neighbors(map, start, width):
    n = []
    value = compatible[map[start] if not map[start].isdigit() else '.']
    checks = [start - 1, start + 1, start - width, start + width]
    for id, idx in enumerate(checks):
        if idx >= 0 and idx < len(map):
            # valid index
            n.append(idx if (map[idx] != '\n' and map[idx] in value[id]) else None)
        else:
            n.append(None)
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
        next_match = get_neighbors(pipe, start, width)
        print(next_match)
        pipe[start] = '0'
        total =  1
        while not all([match is None for match in next_match]) :
            tmp = []
            print(next_match)
            for match in next_match:
                if match is not None:
                    print(match)
                    neighbors = get_neighbors(pipe, match, width)
                    pipe[match] = str(total)
                    for n in neighbors: 
                        tmp.append(n)
            next_match = tmp
            print(next_match)
            total+=1
        print(pipe)
        out = 0
        for i in range(0, len(pipe)):
            if pipe[i].isdigit() and int(pipe[i]) > out:
                out = int(pipe[i]) 
        print(out)



if __name__ == "__main__":
    main()