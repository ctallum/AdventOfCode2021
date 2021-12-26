import numpy as np
import copy

class Board():
    def __init__(self,source):
        self.source = source
        self.board = self.read_data()
        self.step_count = 0

    def get_count(self):
        return self.step_count
    
    def get_board(self):
        return self.board
    
    def read_data(self):
        with open(self.source) as f:
            board = [line.strip() for line in f.readlines()]
            board = [list(line) for line in board]
        return np.array(board)

    def show(self):
        board = [["".join(a)] for a in self.board]
        print(f'After {self.step_count} step:')
        print(np.array(board),'\n')

    def step(self):
        self.step_count += 1
        self.shift('>') 
        self.board = np.transpose(self.board)
        self.shift('v')
        self.board = np.transpose(self.board)
       
    def shift(self,key):
        for row_idx,row in enumerate(self.board):
            # list to keep track of columns that things can't move into
            done = []
            for col_idx, val in enumerate(row):
                # find next column to put char in             
                if col_idx == len(row) - 1: check_idx = 0
                else: check_idx = col_idx + 1
                # check if next column is free and move if it is
                if val == key and row[check_idx] == '.' and col_idx not in done:
                    self.board[row_idx][check_idx] = val
                    self.board[row_idx][col_idx] = '.'
                    # add finished indexes to list to avoid illegal shifting
                    done.append(check_idx)
                    if col_idx == 0:
                        done.append(len(row)-1)

    def save_output(self):
        with open('output.txt','w') as f:
            for line in self.board:
                f.write(''.join(line)+'\n')

data = Board('input.txt')

while True:
    old_board = copy.deepcopy(data.get_board())
    data.step()
    new_board = copy.deepcopy(data.get_board())
    if np.array_equiv(old_board,new_board):
        break
    
data.show()
print(f'Sea Cucumbers stop moving after {data.get_count()}')
data.save_output()