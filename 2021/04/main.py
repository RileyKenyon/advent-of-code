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
        bingo_boards = constructBingoBoards(lines)
        winner_ids = []
        winner_keys = []
        for key in bingo_keys:
            for idx, board in enumerate(bingo_boards):
                if idx not in winner_ids:
                    bingo_boards[idx] = checkOffBingoBoard(board,key)
                    winner = checkForWinner(bingo_boards[idx])
                    if winner:
                        winner_ids.append(idx)
                        winner_keys.append(key)

        if winner_ids:
            # First board to win
            id_first = winner_ids[0]
            key_first = winner_keys[0]
            score_first = calculateWinningScore(bingo_boards[id_first], key_first)
            
            # last board to win
            id_last = winner_ids[-1]
            key_last = winner_keys[-1]
            score_last = calculateWinningScore(bingo_boards[id_last], key_last)
            
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

def checkForWinner(board):
    # initialize default returns
    winner = False
    bingo_type = None

    # Check rows
    for row in board:
        if row.count('x') == len(row):
            winner = True
            bingo_type = 'row'
        
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

    return winner

def calculateWinningScore(board, key):
    # calculates the winning score
    score = 0
    for row in board:
        for val in row:
            score = score + int(val) if val != 'x' else score
    score = score * int(key)
    
    # print out results
    print("Winning Board: {0}".format(board))
    print("Key: {0}".format(key))
    print("Score: {0}".format(score))
    return score


if __name__ == "__main__":
    main()