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

        # do sequence until reaching 'ZZZ'
        search = 'AAA'
        count = 0
        while search != 'ZZZ':
            for lookup in sequence: 
                count+=1
                search = network[search][0 if lookup == 'L' else 1]
                if search == 'ZZZ':
                    break
        print(count)


        
if __name__ == "__main__":
    main()