import math
import sys
import os
import re

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        lines = [list(filter(lambda x: (x if x != '' else []), line.split(':')[1].strip().split(' '))) for line in lines]
        total = 1
        for time, distance in zip(lines[0], lines[1]):
            r1 = range(0, int(time) + 1) 
            r2 = reversed(range(0, int(time) + 1))
            number_of_ways = 0
            for [speed, travel] in zip(r1, r2):
                if speed * travel > int(distance):
                    number_of_ways+=1
            print(number_of_ways)
            total*=number_of_ways 
        print("total: ", total)
        
if __name__ == "__main__":
    main()