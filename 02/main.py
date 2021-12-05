import sys

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        parsed_lines = [line.split(' ') for line in lines]
        path_data = [{"direction": line[0], "amount": int(line[1])} for line in parsed_lines]
        horizontal_location = 0
        depth = 0
        for data in path_data:
            if (data["direction"] == "forward"):
                horizontal_location = horizontal_location + data["amount"]
            elif(data["direction"] == "up"):
                depth = depth - data["amount"]
            elif (data["direction"] == "down"):
                depth = depth + data["amount"]

        result = depth * horizontal_location
        print(result)

if __name__ == "__main__":
    main()