import math
import sys
import os

red_max = 12
green_max = 13
blue_max = 14

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        sum = 0
        lines = f.read().splitlines()
        for line in lines:
            [id, game] = line.split(':')
            id = int(id.strip('Game '))
            draws = game.split(';')
            greens =[]
            blues = []
            reds = []
            max_exceeded = False
            for draw in draws:
                colors = draw.split(',')
                for color in colors:
                    if color.endswith('green'):
                        value = int(color.strip('green '))
                        max_exceeded |= value > green_max
                    elif color.endswith('red'):
                        value = int(color.strip('red '))
                        max_exceeded |= value > red_max
                    else:
                        # blue
                        value = int(color.strip('blue '))
                        max_exceeded |= value > blue_max
            # parse rbg from draws
            # check is any values exceed the max
            # if not add the id to the sum
            if not max_exceeded:
              sum+=id
        print(sum)
        
            
if __name__ == "__main__":
    main()