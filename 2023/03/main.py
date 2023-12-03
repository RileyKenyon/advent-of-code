import math
import sys
import os
import re

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        # Get symbols
        lines = f.read()
        symbols = re.findall('([^\d.\n])', lines)
        unique_symbols = set(symbols)
        
        # Get dimensions of input
        width = len(lines.splitlines()[0]) + 1 # account for newline
        print("Width:", width)

        matches = re.finditer('([^\d.\n])', lines)
        values = []
        for m in matches:
            idx = m.start()
            print("Index match", idx, ": ", lines[m.start()])
            # Check forward / backward
            index = idx - 1
            if lines[index].isdigit():
              start, end = index, index + 1
              while lines[start].isdigit():
                if start == 0:
                    break
                start = start - 1
              while lines[end].isdigit():
                  end = end + 1
              if start != 0:
                  start+=1
              value = int(lines[start:end])
              values.append(value)
              print(start, end, value)
            index = idx + 1
            if lines[index].isdigit():
              start, end = index, index + 1
              while lines[start].isdigit():
                if start == 0:
                    break
                start = start - 1
              while lines[end].isdigit():
                  end = end + 1
              if start != 0:
                  start+=1
              value = int(lines[start:end])
              values.append(value)
              print(start, end, value)

            # check upper row:
            rng = range(idx - 1 - width, idx + 1 - width + 1)
            # any([lines[index].isdigit() for index in rng])
            recent_values = []
            for index in rng:
                # There is at least one match
                start, end = index, index + 1
                if (lines[start].isdigit()):
                  while lines[start].isdigit():
                    if start == 0:
                       break
                    start = start - 1
                  while lines[end].isdigit():
                      end = end + 1
                  if start != 0:
                     start+=1
                  value = int(lines[start:end])
                  if value not in recent_values:
                      recent_values.append(value)
                      print(start, end, value)


            for value in recent_values:
              values.append(value)

            recent_values = []
            rng = range(idx - 1 + width, idx + 1 + width + 1)
            for index in rng:
                # There is at least one match
                start, end = index, index + 1
                if (lines[start].isdigit()):
                  while lines[start].isdigit():
                    if start == 0:
                       break
                    start = start - 1
                  while lines[end].isdigit():
                      end = end + 1
                  if start != 0:
                     start+=1
                  value = int(lines[start:end])
                  if value not in recent_values:
                    recent_values.append(value)
                    print(start,end,value)


            for value in recent_values:
              values.append(value)
            
        print(sum(values))
                
        
            
if __name__ == "__main__":
    main()