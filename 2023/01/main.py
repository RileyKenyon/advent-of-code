import math
import sys
import os
import regex as re

lut = {
  'one' : '1',
  'two' : '2',
  'three' : '3',
  'four' : '4',
  'five' : '5',
  'six' : '6',
  'seven' : '7',
  'eight' : '8',
  'nine' : '9',
  '1' : '1',
  '2' : '2',
  '3' : '3',
  '4' : '4',
  '5' : '5',
  '6' : '6',
  '7' : '7',
  '8' : '8',
  '9' : '9',  
} 

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        sum = 0
        it = 1
        for line in lines:
            matches = re.findall(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)',line, overlapped=True)
            # matches = re.findall(r'(\d)',line)
            print(matches)
            tmp = ''
            if (len(matches) > 1):
                for m in matches[0]:
                    if m:
                        tmp+=lut[m]
                        print(lut[m])
                for m in matches[-1]:
                    if m:
                        tmp+=lut[m]
                        print(lut[m])
            else:
                for m in matches[0]:
                  if m:
                      print(lut[m])
                      if (len(lut[m]) == 1):
                          tmp+=lut[m]
                          tmp+=lut[m]
                      else:
                          tmp+=lut[m]
                      # print(lut[m])
            value = int(tmp)
            print(it, value)
            it+=1
            sum+=value
        print(sum) # too low: 51890, not correct: 54780

if __name__ == "__main__":
    main()