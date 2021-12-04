import numpy as np
from functools import reduce
import re

#Number class
class Num():
    def __init__(self, num : int) -> None:
        self.num = num
        self.chosen = False
    
    def __eq__(self, __o: int) -> bool:
        return self.num == __o
    
    def chosen(self) -> None:
        self.chosen = True

    def get_chosen(self) -> bool:
        return self.chosen

    def __repr__(self) -> str:
        return str(self.num)

#Board class
class Board():
    #Board is a two d numpy array maybe
    def __init__(self, board : np.ndarray) -> None:
        self.board = board

    def __repr__(self) -> str:
        return str(self.board)
    
    def iter(self) -> np.ndarray:
        return self.board

    def check_nums(self, num) -> None:
        for iy, ix in np.ndindex(self.board.shape):
            if self.board[iy, ix] == num:
                self.board[iy, ix].chosen = True
                break
    
    def check_win(self):
        def bool_compare(num1, num2):
            if isinstance(num1, bool):
                return num1 and num2.get_chosen()
            return num1.get_chosen() and num2.get_chosen()

        for row in self.board:
            if reduce(bool_compare, row): return True

        for col in self.board.transpose():
            if reduce(bool_compare, col): return True
        
        return False
        
    def answer_calc(self, winning_num):
        sum = 0
        for iy, ix in np.ndindex(self.board.shape):
            num = self.board[iy, ix]
            if not num.chosen:
                sum += num.num
        return sum*winning_num



bingo = []
boards = []
#Reading in bingo numbs and boards here
with open(file="./Day_4/bingo.txt", mode="r") as f:
    bingo = [int(n) for n in f.readline().split(",")]
    f.readline()
    curr_board = []
    for line in f.readlines():
        if(line == "\n"):
            boards.append(Board(np.array(curr_board)))
            curr_board = []
        else:
            curr_board.append([Num(int(n)) for n in re.findall(r"\d{1,2}", line)])
    boards.append(Board(np.array(curr_board)))
    

def get_winning_board():
    for num in bingo:
        for board in boards:
            board.check_nums(num)
            if board.check_win():
                return (num, board)

def get_last_winning_board():
    winning_num = -1
    winning_board = []
    for num in bingo:
        if len(winning_board) == 100: break
        for b_index, board in enumerate(boards):
            board.check_nums(num)
            if board.check_win():
                if not(b_index in winning_board):
                    winning_board.append(b_index)
                    winning_num = num
    return (winning_num ,boards[winning_board[-1]])

winning_num, board = get_winning_board()
print("Part One\n" + str(board.answer_calc(winning_num)))

winning_num, board = get_last_winning_board()
print("\nPart Two\n" + str(board.answer_calc(winning_num)))







