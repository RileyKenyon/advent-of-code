import sys

def main():
    """
    --- Day 7: The Treachery of Whales ---
    Crab submarines only move horizontally
    List of horizontal position of each crab
    Each 1 step in horizontal position cost fuel
    Find the position that uses the least amount of fuel
    """
    fname = sys.argv[1]
    with open(fname,'r') as f:
        crab_positions = [int(crab) for crab in f.read().split(',')]
        crab_positions.sort()

        # Test every integer between min and maix
        total_distance = sys.maxsize
        for des_pos in range(min(crab_positions), max(crab_positions)+1):
            iter_total_distance = 0
            for pos in crab_positions:                
                crab_distance = abs(pos - des_pos)
                iter_total_distance += (crab_distance * (crab_distance + 1)) //2
            total_distance = min(total_distance, iter_total_distance)
        print(total_distance)

if __name__ == "__main__":
    main()