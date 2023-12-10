import math
import sys
import os
import re
from collections import namedtuple
from functools import reduce
import copy

# Left, Right, Up, Down ( Z are 7)
compatible = {
    'F' : [[], ['J', 'Z', '-'], [], ['J', 'L','|']],
    'J' : [['F', 'L', '-'], [], ['|', 'F', 'Z'], []],
    'Z' : [['F', 'L', '-'], [], [], ['|', 'J', 'L']],
    'L' : [[], ['J', 'Z', '-'], ['|', 'F', 'Z'], []],
    '|' : [[], [], ['F', 'Z','|'], ['J', 'L', '|']],
    '-' : [['F', 'L','-'], ['J', 'Z', '-'], [], []],
    'S' : [['F', 'L', '-'],['J', 'Z', '-'], ['F','Z','|'],['J','L','|']],
    '.' : [[],[],[],[]]
}

def get_neighbors(map, start, width):
    n = []
    value = compatible[map[start] if not map[start].isdigit() and map[start] != 'X' else '.']
    checks = [start - 1, start + 1, start - width, start + width]
    for id, idx in enumerate(checks):
        if idx >= 0 and idx < len(map):
            # valid index
            n.append(idx if (map[idx] != '\n' and map[idx] in value[id]) else None)
        else:
            n.append(None)
    return n

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        pipe = f.read()
        pipe = re.sub('7', 'Z', pipe)
        # print(pipe)
        m = [0] * len(pipe)
        width = len(pipe.split('\n')[0])
        pipe = ''.join(pipe.splitlines())
        start = re.search('S', pipe).start()
        # determine starting pipe type
        pipe = list(pipe)
        original = copy.copy(pipe)
        next_match = get_neighbors(pipe, start, width)
        print(next_match)
        delimeter = 'X'
        pipe[start] = delimeter
        while not all([match is None for match in next_match]) :
            tmp = []
            for match in next_match:
                if match is not None:
                    neighbors = get_neighbors(pipe, match, width)
                    pipe[match] = delimeter
                    for n in neighbors: 
                        tmp.append(n)
            next_match = tmp
        # scan each line
        pipe = list(re.sub('[^X]', '.', ''.join(pipe)))

        # need to region grow
        for i in range(0, len(pipe) // width):
            value = '0'
            for j in range(0, width):
                idx = i * width + j
                if pipe[idx] == 'X':
                    if original[idx] in "|JL" or original[idx] == 'S':
                        value = '0' if value == '1' else '1'
                else:
                    pipe[idx] = value
        print(pipe.count('1'))



if __name__ == "__main__":
    main()