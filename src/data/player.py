from src.data.piece import Piece


class Player:

    def __init__(self, color: str):
        self.color = color
        self.pieces = 12
        self.move_piece = None

    def move(self, board, move_piece: Piece, new_position: tuple):
        self.move_piece = move_piece
        if self.move_piece.king:
            self.move_piece.move_king(board, new_position)
        else:
            self.move_piece.move_regular(board, new_position)
