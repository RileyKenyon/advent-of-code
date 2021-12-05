import math
import sys
import os

sliding_window = 3

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        depth = [int(line) for line in lines]
        count = 0
        for i in range(0, len(depth) - sliding_window):
            sum1 = sum(depth[i + 1 : i + 1 + sliding_window])
            sum2 = sum(depth[i : i+sliding_window])
            count = count + 1 if sum1 > sum2 else count

    print(count)

if __name__ == "__main__":
    main()