import numpy as np
from pieces import *
from colorama import init, Fore, Back

init()

row_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
column_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

class Board:
    def __init__(self, board_arrangement):
        self.turn = 0
        self.color = 'white'
        self.board = np.array(board_arrangement)
                

        
    def flip(self):
        self.board = np.rot90(self.board)
        self.board = np.rot90(self.board)
        if self.color == 'white':
            self.color == 'black'
        elif self.color == 'black':
            self.color = 'white'
            
        
    def make_move(self, pos_1, pos_2):
        piece = self.board[pos_1[0]][pos_1[1]]
        if piece.tolist() == [Xx, Xx]:
            return False
        if self.board[pos_2[0]][pos_2[1]].tolist() == [Xx, Xx] and piece[0].move(pos_1, pos_2, self, piece[0]): # If piece can make the move
            print('can move')
            piece[0].move_num += 1
            self.board[pos_2[0]][pos_2[1]] = piece # Move piece to new space
            self.board[pos_1[0]][pos_1[1]] = (Xx, Xx) # Set the original space to blank
            
        elif piece[0].capture(pos_1, pos_2, self, piece):
            
            print('can capture')
            piece[0].move_num += 1
            self.board[pos_2[0]][pos_2[1]] = piece
            self.board[pos_1[0]][pos_1[1]] = (Xx, Xx)
        else:
            print('cannot move')
            return False
            
    def pprint(self):
        row_to_print = ''
                # Iterate through each item and add the column and row letters/numbers
        for i in range(len(self.board)):
            row_to_print += column_numbers[i] # Add the 
            row_to_print += ' ' # Space out numbers from board            
            for j in range(len(self.board[0])):
                if self.board[i][j][0] is None: # If there isn't a piece on the current square
                    
                    # Do the checkerboard thing                    
                    if (i+j) % 2:
                        row_to_print += '██'                        
                    else:
                        row_to_print += '  '

                else:
                    
                    if self.board[i][j][1] is WH:
                        row_to_print += Fore.BLACK + Back.WHITE + self.board[i][j][0].symbol + Fore.RESET + Back.RESET
                    elif self.board[i][j][1] is BL:
                        row_to_print += Fore.WHITE + Back.BLACK + self.board[i][j][0].symbol + Fore.RESET + Back.RESET

            row_to_print += '\n'
        row_to_print += ' ' * len(column_numbers[0]) + ' ' # Adding numbers on left moves everything over by two spaces
        row_to_print += " ".join(row_letters[:len(self.board[0])]) # Add letters to the bottom
        print(row_to_print)


        
def parse_code(inp): # To convert 'A01 B02' to 2D list indices
    global chessboard
    
    pos_1, pos_2 = inp.split(' ')
    
    x1 = column_numbers.index(pos_1[1:])
    y1 = row_letters.index(pos_1[0])
    
    x2 = column_numbers.index(pos_2[1:])
    y2 = row_letters.index(pos_2[0])
    
    return x1, y1, x2, y2