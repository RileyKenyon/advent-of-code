import sys
from itertools import permutations

def main():
    """
    --- Day 8: Seven Segment Search ---
    Four digit seven segment displays in submarine
    Segments a-g are used to render each digit, but are mixed up
    Display has different mapping, for instance b & g could be active
    but that would represent 1 since it is the only one that uses two digits.
    Ten unique signal patterns are collected, delimited by '|'. 
    1.) Find the mapping and count the number of times unique digits (1,4,7,8) appear
    """
    default_dict = {
        'abcefg' : '0',
        'cf' : '1',
        'acdeg' : '2',
        'acdfg' : '3',
        'bcdf' : '4',
        'abdfg' : '5',
        'abdefg' : '6',
        'acf' : '7',
        'abcdefg' : '8',
        'abcdfg' :'9'
    }
    cumsum = 0
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Perform this set of operations for each line entry
        for line in f.read().splitlines():
            # Decode line
            [patterns, codes] = line.split('|')
            
            # Need to do permutations of different mappings
            default_string = "abcdefg"
            for p in permutations(default_string):
                mapping = {key: val for key,val in zip(p, default_string)}
                result = {"".join(sorted(map(mapping.get, pattern))) for pattern in patterns.split()}

                # Check if permutation has the right mapping
                if result == default_dict.keys():
                    # Decode the coded values
                    code_result = ["".join(sorted(map(mapping.get,code))) for code in codes.split()]
                    cumsum = cumsum + int("".join([(default_dict.get(combo)) for combo in code_result]))
        print(cumsum)

if __name__ == "__main__":
    main()