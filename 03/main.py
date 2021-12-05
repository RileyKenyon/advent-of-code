import sys
import numpy as np

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        oxBit = int(getOxygenBits(lines),2)
        coBit = int(getCO2Bits(lines),2)
        print(oxBit * coBit)
    
def getOxygenBits(codes):
    idx = 0
    while (len(codes) > 1) and (idx < len(codes[0])):
        idxArr = [int(line[idx]) for line in codes]
        filterVal =  [1 if sum(idxArr) >= len(codes)/2 else 0]
        logicalIdx = np.array(idxArr) == filterVal
        codes = np.array(codes)[logicalIdx]
        idx = idx + 1
    return "".join(codes)

def getCO2Bits(codes):
    idx = 0
    while (len(codes) > 1) and (idx < len(codes[0])):
        firstIdxArr = [int(line[idx]) for line in codes]
        filterVal = [1 if sum(firstIdxArr) < len(codes)/2 else 0]
        logicalIdx = np.array(firstIdxArr) == filterVal
        codes = np.array(codes)[logicalIdx]
        idx = idx + 1
    return "".join(codes)

if __name__ == "__main__":
    main()