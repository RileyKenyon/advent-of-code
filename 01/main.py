import math
import sys
import os


def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        depth = [int(line) for line in lines]
        count = 0
        for i in range(0, len(depth) - 1):
            count = count + 1 if depth[i+1] > depth[i] else count

    print(count)

if __name__ == "__main__":
    main()