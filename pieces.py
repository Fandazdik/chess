import numpy as np
from collections import Counter

WH, BL = range(2)

class Piece: # Defines a new piece
    def __init__(self, name, abbreviation, symbol, valid_move, valid_capture, promotion_limit = None):
        self.name = name
        self.abbrev = abbreviation
        self.symbol = symbol
        self.move = valid_move
        self.capture = valid_capture
        self.move_num = 0
        
def rook_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    if pos_1 == pos_2:
        return False
    if pos_1 != pos_2:
        if pos_1[0] == pos_2[0]:
            for i in range(pos_1[1]):
                print(board.board[pos_1[0]][i])
            return True
        elif pos_1[1] == pos_2[1]:
            for i in range(pos_1[0]):
                print(board.board[pos_1[1]][i])
            return True
    return False

def king_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    if pos_1 == pos_2:
        return False
    move_difference = np.array(pos_1) - np.array(pos_2)
    if -1 <= move_difference[0] <= 1 and -1 <= move_difference[1] <= 1:
        return True
    else:
        return False
    
def bishop_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    if pos_1 == pos_2:
        return False
    move_difference = np.array(pos_1) - np.array(pos_2)
    print(move_difference)
    if abs(move_difference[0]) == abs(move_difference[1]):
        for x in range(1, move_difference[0]):
            for y in range(1, move_difference[1]):
                if board.board[x][y].tolist() != [Xx, Xx]:
                    return False
                next
        return True
    else:
        return False


def pawn_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    if pos_1 == pos_2:
        return False
    move_difference = np.array(pos_1) - np.array(pos_2)
    print(piece_stats.move_num)
    print(move_difference)
    if move_difference.tolist() == [1, 0] or move_difference.tolist() == [2, 0]:
        return True
    else:
        False
    
def pawn_valid_capture(pos_1, pos_2, board = None, piece_stats = None):
    if pos_1 == pos_2:
        return False
    move_difference = np.array(pos_1) - np.array(pos_2)
    print(move_difference.tolist() == [1, 1])
    print(move_difference.tolist() == [1, -1])
    if (move_difference.tolist() == [1, 1]) or (move_difference.tolist() == [1, -1]):
        return True
    else:
        return False
    
def queen_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    return bishop_valid_move(pos_1, pos_2, board) or rook_valid_move(pos_1, pos_2, board)
    
def knight_valid_move(pos_1, pos_2, board = None, piece_stats = None):
    move_difference = np.array(pos_1) - np.array(pos_2)
    move_difference = abs(move_difference)
    if Counter(move_difference) == Counter([1, 2]):
        return True
    else:
        return False


Rk = Piece('rook', 'rk', '♖', rook_valid_move, rook_valid_move)
Pw = Piece('pawn',  'pw', '♙', pawn_valid_move, pawn_valid_capture)
Bi = Piece('bishop', 'bi', '♗', bishop_valid_move, bishop_valid_move)
Ki = Piece('king', 'ki', '♚', king_valid_move, king_valid_move)
Qu = Piece('queen', 'qu', '♛', queen_valid_move, queen_valid_move)
Kn = Piece('knight', 'kn', '♘', knight_valid_move, knight_valid_move)
Xx = None