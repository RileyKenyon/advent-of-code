import sys

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
        lines = f.read().splitlines()
        gamma = []
        epsilon = []
        for idx in range(0, len(lines[0])):
            id_sum = sum([int(line[idx]) for line in lines])
            temp = 1 if id_sum > len(lines)/2 else 0
            gamma.append(str(temp))
            epsilon.append(str(~temp & 0x01))
            
        gamma_int = int("".join(gamma),2)
        epsilon_int=  int("".join(epsilon),2)
        print(gamma_int * epsilon_int)

if __name__ == "__main__":
    main()