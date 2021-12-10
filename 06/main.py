import sys

def main():
    """
    --- Day 6: Lanternfish ---
    Lanternfish create new lanternfish every 7 days
    Each fish can be represented a number of days until it creats a new fish
    Determine the number of points that have at least two lines overlap
    
    Counter -> 7..0,6
    New_counter -> 8..0,6

    List given with 100 nearby ages
    When fish hits 0, addnew fish with 8, resets self to 6

    Determine how many fish after 80 days
    """
    num_days = 80
    old_lifespan = 6
    new_lifespan = 8
    fname = sys.argv[1]
    with open(fname,'r') as f:
        day_counter = [0 for i in range(0,new_lifespan + 1)]
        for fish in map(int,f.read().split(',')):
            day_counter[fish]+=1

        for day in range(0,num_days):
            next_day = [0 for i in range(0,new_lifespan +1 )]
            for idx, num_fish in enumerate(day_counter):
                if idx == 0:
                    next_day[new_lifespan]+= num_fish
                    next_day[old_lifespan]+= num_fish
                else:
                    next_day[idx-1]+= num_fish
            day_counter = next_day
        print(sum(day_counter))

        
if __name__ == "__main__":
    main()