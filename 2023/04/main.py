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
        number_of_cards = [1]* len(lines)
        for id, pair in enumerate(lines):
            for _ in range(0, number_of_cards[id]):
              winning = pair[0].strip().split(' ')
              winning = [value if value != '' else [] for value in winning]
              my_numbers = pair[1].strip().split(' ')
              count = 0
              for num in my_numbers: 
                  if num in winning:
                      count+=1
                      if (count + id < len(lines)):
                        number_of_cards[count + id]+=1
        print("total", sum(number_of_cards))
        
if __name__ == "__main__":
    main()