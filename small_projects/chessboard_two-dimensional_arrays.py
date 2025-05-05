# This program uses two-dimensional arrays (matrix) and list comprehension to output
# a chessboard with unicode characters

# Although it would have been easier to leave the squares in the centre blank,
# I decided to challenge myself to manually alternate the black and white squares.

board = []

WHITE_SQUARE = "⬜"
BLACK_SQUARE = "⬛"

# Creates an 8x8 board using list comprehension, with logic to alternate between
# black and white squares.
# The alternating colours are determined by the sum of row and column indices.
# If the sum of row and column is even, it's a white square; if odd, it's black.
# The board variable is a two-dimensional array/matrix (using nested list comprehension)
board = [[WHITE_SQUARE if (row + col) % 2 == 0 else BLACK_SQUARE for col in range(8)]
         for row in range(8)]


# ♙ White pieces - symbols and unicode
# ♔ U+2654 – King
# ♕ U+2655 – Queen
# ♖ U+2656 – Rook
# ♗ U+2657 – Bishop
# ♘ U+2658 – Knight
# ♙ U+2659 – Pawn

# ♟ Black pieces - symbols and unicode
# ♚ U+265A – King
# ♛ U+265B – Queen
# ♜ U+265C – Rook
# ♝ U+265D – Bishop
# ♞ U+265E – Knight
# ♟ U+265F – Pawn


# --- BLACK PIECES ---
# Note: I've added spaces to some pieces to ensure proper alignment in the output
# the output isn't perfect, but it was as close as I could get

# Black Pawns
board[1] = ["♟"] * 8
board[1][0] = "♟    "
board[1][1] = "♟    "
board[1][3] = "♟    "
board[1][5] = "♟    "

# Black Rooks
board[0][0] = "♜    "
board[0][7] = "♜"

# Black Knights
board[0][1] = "♞    "
board[0][6] = "♞"

# Black Bishops
board[0][2] = "♝"
board[0][5] = "♝    "

# Black King/Queen
board[0][3] = "♛    "
board[0][4] = "♚"


# --- WHITE PIECES ---

# White Pawns
board[6] = ["♙"] * 8
board[6][0] = "♙    "
board[6][1] = "♙    "
board[6][3] = "♙    "
board[6][5] = "♙    "

# White Rooks
board[7][0] = "♖    "
board[7][7] = "♖"

# White Knights
board[7][1] = "♘    "
board[7][6] = "♘"

# White Bishops
board[7][2] = "♗"
board[7][5] = "♗    "

# White King/Queen
board[7][3] = "♕    "
board[7][4] = "♔"


# Outputs the board with a format that ensures alignment
# Each square is padded with 4 spaces in columns for visual consistency
for row in board:
    print(" ".join(f"{square:4}" for square in row))
