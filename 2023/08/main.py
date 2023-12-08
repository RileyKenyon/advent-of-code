import math
import sys
import os
import re
from collections import namedtuple


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
        count = 0
        while not all([search.endswith('Z') for search in search_keys]):
            for lookup in sequence: 
                count+=1
                for id, search in enumerate(search_keys):
                    search_keys[id] = network[search][0 if lookup == 'L' else 1]
        print(count)


        
if __name__ == "__main__":
    main()