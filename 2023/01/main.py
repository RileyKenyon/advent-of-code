import math
import sys
import os
import re
def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        sum = 0
        for line in lines:
            value = re.sub(r'[a-z]|[A-Z]','',line)
            if (len(line) > 1):
                value = int(value[0] + value[-1])
            else:
                value = int(value)
            sum+=value
        print(sum)

if __name__ == "__main__":
    main()