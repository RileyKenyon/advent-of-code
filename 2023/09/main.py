import math
import sys
import os
import re
from collections import namedtuple
from functools import reduce

def diff(line):
    l = []
    it = iter(line)
    l1 = next(it)
    l2 = next(it)
    try:
        while True:
            l.append(l2 - l1)
            l1 = l2
            l2 = next(it)
    except StopIteration:
        pass
    # print(l)
    return l

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        lines = [line.split(' ') for line in lines]
        lines = [[int(num) for num in line] for line in lines]
        print(lines)
        out = 0
        for line in lines:
            save = []
            while not all([l == 0 for l in line]):
                save.append(line[-1])
                line = diff(line)
            out+=reduce(lambda x,y: x + y, save)
        print(out)
                
                

                
            

if __name__ == "__main__":
    main()