import sys

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
    mapping_dict = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
    }
    default_dict = {
        "0": ['a','b','c','e','f','g'],
        "1": ['c','f'],
        "2": ['a','c','d','e','g'],
        "3": ['a','c','d','f','g'],
        "4": ['b','c','d','f'],
        "5": ['a','b','d','f','g'],
        "6": ['a','b','d','e','f','g'],
        "7": ['a','c','f'],
        "8": ['a','b','c','d','e','f','g'],
        "9": ['a','b','c','d','f','g'],
    }
    decode_dict = {
        "0" : [],
        "1" : [],
        "2" : [],
        "3" : [],
        "4" : [],
        "5" : [],
        "6" : [],
        "7" : [],
        "8" : [],
        "9" : []
    }
    # counting_dict = {
    #     "0" : 0,
    #     "1" : 0,
    #     "2" : 0,
    #     "3" : 0,
    #     "4" : 0,
    #     "5" : 0,
    #     "6" : 0,
    #     "7" : 0,
    #     "8" : 0,
    #     "9" : 0
    # }
    counter = 0
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Perform this set of operations for each line entry
        for line in f.read().splitlines():
            # Decode line
            [patterns, code] = line.split('|')
            patterns = patterns.split()
            code = code.split()
        
            # Sort entries 
            sorted_patterns = sorted(patterns,key=len)
            sorted_codes = sorted(code,key=len)
            
            for pattern in sorted_codes:
                # Unique pattern matching
                l_pattern = len(pattern)
                if l_pattern in [2,4,3,7]:
                    counter = counter + 1
        print(counter)
            # sorted_patterns = [sorted(entry) for entry in sorted(patterns, key=len)]
            # sorted_code = [sorted(entry) for entry in sorted(code, key=len)]
            
            # Look at length of input array
            # see if it matches the length of the default dictionary
            # If so, loop through elements
            # see if mapping has an entry
            # if it does remove the element from the input array
            # if it does not and the number of elements in the array is 1
            # assign the element from the input array to the mapping

            # Map to elements
            # for key in default_dict:
            #     dict_item = default_dict[key]
            #     # While patterns exist
            #     while (pattern):
            #         for pattern in sorted_patterns:
            #             if len(pattern) == len(dict_item):
            #                     for element in pattern:
            #                         if not mapping_dict[element]:
                                

            # for pattern in sorted_patterns:
            #     # Unique pattern matching
            #     for i in range(0,len(pattern)):
            #         if not mapping_dict(pattern[i]):
            #             mapping_dict(pattern[i]) = pattern[i]
            #     decode_dict["1"] = pattern if len(pattern) == 2 else decode_dict["1"]
            #     decode_dict["4"] = pattern if len(pattern) == 4 else decode_dict["4"]
            #     decode_dict["7"] = pattern if len(pattern) == 3 else decode_dict["7"]
            #     decode_dict["8"] = pattern if len(pattern) == 8 else decode_dict["8"]
            
                # Remainder 
                # while 
            # Debugging
            # for key in default_dict:
            #     print("{0}: {1}, {2}".format(key,default_dict[key],decode_dict[key]))
            
        # Digits with unique number of entries
        # 2 == len(1)
        # 4 == len(4)
        # 3 == len(7)
        # 7 == len(8)
        # one_entries = sorted_patterns[len_array == 2]
        # four_entries = sorted_patterns[len_array == 4]
        # seven_entries = sorted_patterns[len_array == 3]
        # eight_entries = sorted_patterns[len_array == 8]

        # print(eight_entries)

if __name__ == "__main__":
    main()