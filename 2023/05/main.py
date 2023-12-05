import math
import sys
import os
import re
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
from collections import namedtuple
MapValue = namedtuple('MapValue', ['dst', 'start', 'length']) 
Seed = namedtuple('Seed', ['start', 'end'])
seed_map = []

def get_map(content):
    m = {}
    for item in content:
        item = item.split(' ')
        dst = int(item[0])
        start = int(item[1])
        length = int(item[2])
        for i in range(length):
            m[start + i] = dst + i
    return m

def map_lookup(value, map):
    output_value = value
    for m in map:
        if value >= m.start and value < m.start + m.length:
            output_value = m.dst + (value - m.start)
    return output_value

def is_map_in_range(seeds, map):
    # 3 cases
    # 1 - [start --> map.start], m[map.start --> end]
    # 2 - [start --> end]
    # 3 - m[start --> map.end], [map.end --> end]
    output_value = []
    for seed in seeds:
        matchFound = False
        rem = Seed(seed.start, seed.end)
        for m in map:
            # some form of overlap
            if (seed is not None and seed.end > m.start and seed.start < m.start + m.length - 1):
                # print(m, seed)
                d1 = m.start + m.length - 1 - seed.start
                d2 = seed.end - m.start
                # print(d1, d2)
                overlap = Seed(seed.start, seed.end)
                if d1 > m.length and d2 > m.length:
                    # full overlap
                    rem = None
                    # overlap = Seed(m.start, m.start + m.length)
                    overlap = Seed(m.dst, m.dst + m.length - 1)
                    matchFound = True
                elif d1 > m.length:
                    # Right overlap
                    # overlap = Seed(m.start, seed.end)
                    overlap = Seed(m.dst, m.dst + (seed.end - m.start))
                    rem = Seed(seed.start, seed.end - m.start + seed.start)
                    matchFound = True
                elif d2 > m.length:
                    # left overlap
                    # overlap= Seed(seed.start, m.start + m.length)
                    overlap = Seed(seed.start - m.start + m.dst, m.dst + m.length - 1)
                    rem = Seed(m.start + m.length, seed.end)
                    matchFound = True
                else:
                    overlap = Seed(seed.start - m.start + m.dst, seed.end - m.start + m.dst)
                    rem = None
                    matchFound = True
                # print(overlap, rem)
                if matchFound:
                    seed = rem
                    output_value.append(overlap)
        if matchFound == False:
            output_value.append(seed)
    return output_value

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().split('\n\n')
        for idx, line in enumerate(lines):
            content = line.split(':')[1].strip().splitlines()
            if (idx == 0):
                seeds = content[0].split(' ')
                seeds = [int(seed) for seed in seeds]
                for i in range(0, len(seeds), 2):
                    tmp = Seed(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1)
                    if len(seed_map) > 0:
                        for id, seed in enumerate(seed_map):
                            if tmp.end > seed.start and tmp.end <= seed.end:
                                # can combine
                                seed_map[id] = Seed(tmp.start, seed.end)
                            elif tmp.start > seed.start and tmp.end >= seed.end:
                                # can combine
                                seed_map[id] = Seed(seed.start, tmp.end)
                            else:
                                seed_map.append(tmp)
                    else:
                        seed_map.append(tmp)
                print("seeds: ", seeds)
            if (idx == 1):
                for item in content:
                    item = item.split(' ')
                    seed_to_soil.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 2):
                for item in content:
                    item = item.split(' ')
                    soil_to_fertilizer.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 3):
                for item in content:
                    item = item.split(' ')
                    fertilizer_to_water.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 4):
                for item in content:
                    item = item.split(' ')
                    water_to_light.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 5):
                for item in content:
                    item = item.split(' ')
                    light_to_temperature.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 6):
                for item in content:
                    item = item.split(' ')
                    temperature_to_humidity.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
            if (idx == 7):
                for item in content:
                    item = item.split(' ')
                    humidity_to_location.append(MapValue(int(item[0]), int(item[1]), int(item[2])))
        min_value = 1000000000000000000000
        seed = seed_map
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, seed_to_soil)
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, soil_to_fertilizer)
        seed = is_map_in_range(seed, fertilizer_to_water)
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, water_to_light)
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, light_to_temperature)
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, temperature_to_humidity)
        print(seed) # somehow end is before start
        seed = is_map_in_range(seed, humidity_to_location)
        print(seed) # somehow end is before start
        for s in seed:
            min_value = min(s.start, min_value)
        print(min_value)







        
        
if __name__ == "__main__":
    main()