# chess
Program / Module that allows for custom pieces and chess board arrangements to be made.

Note: `game.py` *is a small implementation of a game, but is not entirely finished.*
### `game.py` todo:
- Add function that alerts when Check / Checkmate etc.
- Add easier way to type in piece moves than A1 B2 etc.
- Do not change player if they make an invalid move

## How to add pieces and board arrangements
*Clean up.*
- Make function to check if a piece can move or capture in `pieces.py` with the start position, target position, and Board object (to access chessboard array). Please note that piece movement will take place from the final row in the array to the 0th array.
- Create a variable (preferably two letters long) as `Piece` object with input for `name, abbreviation (usually same as variable name), symbol to use on chessboard, function to check if move is valid, function to check if capture is valid`.
- In `modes.py`, create a new dictionary entry with a key value pair of the name of the board arrangement, followed by a 2D array of the initial positions of the pieces, in the form `(variable for piece name, player_colour)` where BL is the Black player and WH is the White player. Blank spaces may be represented with `(Xx, Xx)`
- In `game.py`, create an instance of `Board` with `modes.modes['your arrangement name here']`, which will then be shown in the console.
- Input can be taken in the form 'A4 B2' or similar, where a piece on the A4 square is to be moved to B2. 

## Class `Board`
#### Board.pprint()
Displays chess board in console.
#### Board.flip()
Changes rotation of board.
#### Board.make_move(pos_1, pos_2)
Attempt move from piece on `pos_1` to `pos_2`.
If move is successful, move will be made. Otherwise, nothing will happen.
#### Board.color
Current player's move.
#### Board.board
Current board arrangement.
