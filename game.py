import numpy as np
from collections import Counter

from chess import *
import modes

init()


chessboard = Board(modes.modes['demichess'])

# Game Loop
while 1:
     
     # White's turn
     
     valid_move = True

     chessboard.pprint()
     next_move = input()
     
     x1, y1, x2, y2 = parse_code(next_move)
     
     res = chessboard.make_move([x1, y1], [x2, y2])
     chessboard.flip()

     # Black's turn
     print('\n')
     print(f'{chessboard.color}\'s turn')
     chessboard.pprint()
     next_move = input()
     
     x1, y1, x2, y2 = parse_code(next_move)
     
     chessboard.make_move([x1, y1], [x2, y2])
     chessboard.flip()
     
     chessboard.turn += 1
     print('\n')
    


