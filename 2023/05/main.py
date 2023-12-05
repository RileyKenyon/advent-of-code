import math
import sys
import os
import re
seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
from collections import namedtuple
MapValue = namedtuple('MapValue', ['dst', 'start', 'length']) 
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

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().split('\n\n')
        for idx, line in enumerate(lines):
            content = line.split(':')[1].strip().splitlines()
            if (idx == 0):
                seeds = content[0].split(' ')
                seeds = [int(seed) for seed in seeds]
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
        location = []
        for seed in seeds:
            value = map_lookup(seed, seed_to_soil)
            value = map_lookup(value,soil_to_fertilizer)
            value = map_lookup(value, fertilizer_to_water)
            value = map_lookup(value, water_to_light)
            value = map_lookup(value, light_to_temperature)
            value = map_lookup(value, temperature_to_humidity)
            value = map_lookup(value, humidity_to_location)
            location.append(value)
        print(min(location))







        
        
if __name__ == "__main__":
    main()