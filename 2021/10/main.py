import sys

def main():
    """
    --- Day 10: Syntax Scoring ---
    Navigation subsystem syntax is made of several lines containing chunks
    Chunks can contain other chunks
    Adjacent chunks are not specified by a delimeter
    Every chunk must open and close with one of four legal pairs
    ( with )
    [ with ]
    { with }
    or < with >
    Some lines are incomplete but others are corrupted - find and discard the corrupted lines first
    Corrupted closes with the wrong characters (]
    Incomplete lines can be ignored
    Stop at the first incorrect closing character on each corrupted line
    """
    point_lookup = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4,
    }
    close_lookup  = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '>' : '<'
    }
    start_lookup  = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }
    total_sum = 0
    sum_list = []
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Split lines, convert into 2D array
        raw_lines = f.read().splitlines()
        for id, line in enumerate(raw_lines):
            start_char = []
            end_char = []
            for cid, char in enumerate(line):
                if char in '([{<':
                    start_char.append(char)
                elif char in ')]}>':
                    match_char = start_char.pop()
                    if match_char != close_lookup[char]:
                        # print("{0}:{1} Un-matched character {2}".format(id,cid,char))
                        # total_sum += point_lookup[char]
                        start_char = []
                        break
                    else:
                        # if it does match, put it back
                        end_char.append(end_char)
                else:
                    print("Invalid Character: {0}".format(char))
                    return
            if start_char != []:
                for char in start_char[::-1]:
                    total_sum*= 5
                    total_sum+= point_lookup[start_lookup[char]]
                sum_list.append(total_sum)
                total_sum = 0
    sum_list.sort()
    print(sum_list[len(sum_list) // 2])

if __name__ == "__main__":
    main()