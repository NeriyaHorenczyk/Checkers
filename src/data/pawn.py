from src.data.board import Board
from src.data.piece import Piece

class Pawn(Piece):

    def __init__(self, color: str, position: tuple[int, int]):
        super().__init__(color)
        self.position = position

    def move(self, board : Board, new_position : tuple[int, int]):
        if self.is_valid_move(board, new_position):
            self.position = new_position

    def capture(self, board : Board, new_position : tuple[int, int]):
        if self.is_valid_capture(board, new_position):
            # Remove the captured piece from the board
            captured_position = ((self.position[0] + new_position[0]) // 2,
                                 (self.position[1] + new_position[1]) // 2)
            board[captured_position[0]][captured_position[1]] = "_"
            self.position = new_position

    def is_valid_move(self, board : Board, new_position : tuple[int, int]):

        if new_position[0] < 0 or new_position[0] > 7 or new_position[1] < 0 or new_position[1] >= 7:
            return False

        row_diff = new_position[0] - self.position[0]
        col_diff = new_position[1] - self.position[1]

        if self.color == 'white':
            return row_diff == 1 and abs(col_diff) == 1
        return row_diff == -1 and abs(col_diff) == 1

    def is_valid_capture(self, board : Board, new_position : tuple[int, int]):
        row_diff = new_position[0] - self.position[0]
        col_diff = new_position[1] - self.position[1]

        if abs(row_diff) == 2 and abs(col_diff) == 2:
            captured_position = ((self.position[0] + new_position[0]) // 2,
                                 (self.position[1] + new_position[1]) // 2)
            captured_piece = board[captured_position[0]][captured_position[1]]
            return captured_piece is not None and captured_piece.color != self.color

        return False
