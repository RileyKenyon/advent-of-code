import math
import sys
import os
import re

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Get symbols
        lines = f.read().splitlines()
        lines = [line.split(':')[1].split('|') for line in lines]
        both = [[line[0].strip().split(' '), line[1].strip().split(' ')] for line in lines]
        total_score = 0
        for pair in lines:
            winning = pair[0].strip().split(' ')
            winning = [value if value != '' else [] for value in winning]
            my_numbers = pair[1].strip().split(' ')
            score = 0
            matches = []
            for num in my_numbers: 
                if num in winning:
                    matches.append(num)
                    score = 1 if score == 0 else score*2
            total_score+=score
            print("Score: ", score, matches)
        print("total", total_score)

        
        # first match is one point
        # Subsequent matches doubles the point value of the card
        # 159074 - not right


if __name__ == "__main__":
    main()