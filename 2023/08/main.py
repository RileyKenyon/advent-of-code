import math
import sys
import os
import re
from collections import namedtuple
from functools import reduce
from math import gcd

def lcm(nums):
    return reduce(lambda x,y: x*y // gcd(x,y), nums)

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        sequence = lines[0].strip()
        lines = lines[2::]
        print("Sequence: ", sequence)
        # construct network
        network = {}
        for line in lines:
            if line != '':
                key, value = line.split('=')
                values = value.strip('( )').split(',')
                values = [value.strip() for value in values] 
                network[key.strip()] = values
        print(network)

        # Get keys that end in A
        search_keys = list(filter(lambda x: x.endswith('A'), network.keys()))

        # do sequence until reaching 'ZZZ'
        counters = [0] * len(search_keys)
        for id, search in enumerate(search_keys):
            count = 0
            while not search.endswith('Z'):
                for lookup in sequence: 
                    count+=1
                    search = network[search][0 if lookup == 'L' else 1]
                    if search.endswith('Z'):
                        break
                print(search)
            counters[id] = count

        # Find lcm
        print(lcm(counters))


        
if __name__ == "__main__":
    main()