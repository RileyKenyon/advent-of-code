import sys
import numpy as np
import copy

def main():
    fname = sys.argv[1]
    with open(fname,'r') as f:
    # To convert the text into bingo boards
    # 1. Split file by double line endings
    # 2. Append arrays along 2nd dimention until empty string is reached ''
    # 3. index to next array
    # 4. repeat until end of file        
        lines = f.read().split('\n\n')
        bingo_keys = lines.pop(0)
        bingo_keys = bingo_keys.split(',')
        original_bingo_boards = constructBingoBoards(lines)
        bingo_boards = copy.deepcopy(original_bingo_boards)
        for key in bingo_keys:
            for id, board in enumerate(bingo_boards):
                bingo_boards[id] = checkOffBingoBoard(board,key)
                if id == 0:
                    print(key)
                    print(bingo_boards[59])
            winner, id = checkForWinners(bingo_boards)
            if winner:
                break

        if winner:
            score = calculateWinningScore(bingo_boards[id], key)
            print("Winning Board Id: {0}".format(id))
            print("Key: {0}".format(key))
            print("Score: {0}".format(score))
            print(bingo_boards[id])
            print(original_bingo_boards[id])
        else:
            print("No Winning board")




def constructBingoBoards(rawFile):
    # raw file with bingo keys removed - string bingo array with line returns
    str_arr = [line.split('\n') for line in rawFile]
    bingo_arr = []
    # string bingo 2D array with each row as a string
    for arr in str_arr:
        # Split array into elements
        inner_bingo_arr = []
        for row in arr:
            bingo_line_vals = row.split(' ')
            # Remove any additional spaces
            while '' in bingo_line_vals:
                bingo_line_vals.remove('')
            # int_arr = [int(val) for val in bingo_line_vals]
            inner_bingo_arr.append(bingo_line_vals)
        bingo_arr.append(inner_bingo_arr)
    return bingo_arr

def checkOffBingoBoard(board, key):
    # Check un-wrap board
    newboard = []
    for row in board:
        row = ['x' if val == key else val for val in row]
        newboard.append(row)
    return newboard


def checkForWinners(boards):
    # initialize default returns
    winner = False
    id = None
    bingo_type = None
    for id, board in enumerate(boards):
        # Check rows
        for row in board:
            if row.count('x') == len(row):
                winner = True
                bingo_type = 'row'
                break
        
        # Check columns
        col_id = []
        counter_arr = [0 for i in range(0,len(board))]
        for row in board:
            for val_id, val in enumerate(row):
                if val == 'x':
                    # log id, make sure other winners match
                    if (val_id not in col_id):
                        col_id.append(val_id)
                    counter_arr[val_id] = counter_arr[val_id] + 1

        if (counter_arr.count(len(board))):
            winner = True
            bingo_type = 'column'
        
        if winner:
            break
   
    # Return results
    # print(winner, bingo_type, id)
    return winner, id

def calculateWinningScore(board, key):
    # calculates the winning score
    score = 0
    for row in board:
        for val in row:
            score = score + int(val) if val != 'x' else score
    return score * int(key)


if __name__ == "__main__":
    main()