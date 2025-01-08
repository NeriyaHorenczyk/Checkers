from src.data.king import King
from src.data.piece import Piece, Color

class Pawn(Piece):

    def move(self, board, new_position: list[int]) -> bool:
        row_diff = new_position[0] - self.position[0]
        col_diff = new_position[1] - self.position[1]

        if self.color == Color.WHITE:  # White pawns move down
            valid_move = row_diff == -1 and abs(col_diff) == 1
        else:  # Black pawns move up
            valid_move = row_diff == 1 and abs(col_diff) == 1

        if valid_move and board[new_position] == "_":
            self.position = new_position

            # Check for promotion
            if (self.color == Color.WHITE and self.position[0] == 7) or \
                    (self.color == Color.BLACK and self.position[0] == 0):
                self.promote_to_king(board)

            return True
        return False

    def promote_to_king(self, board):
        board[self.position] = King(self.color, self.position)

    def capture(self, board, new_position: list[int]) -> bool:
        row_diff = new_position[0] - self.position[0]
        col_diff = new_position[1] - self.position[1]

        if abs(row_diff) == 2 and abs(col_diff) == 2:
            captured_position = ((self.position[0] + new_position[0]) // 2, (self.position[1] + new_position[1]) // 2)
            captured_piece = board[captured_position]

            if captured_piece != "_" and captured_piece.color != self.color:
                self.position = new_position
                board[captured_position] = "_"
                return True
        return False

    def can_move(self, board) -> bool:
        directions = [(1, 1), (1, -1)] if self.color == Color.WHITE else [(-1, 1), (-1, -1)]
        for direction in directions:
            new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
            if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and board[new_position] == "_":
                return True
        return False

    def can_capture(self, board) -> bool:
        directions = [(2, 2), (2, -2)] if self.color == Color.WHITE else [(-2, 2), (-2, -2)]
        for direction in directions:
            new_position = [self.position[0] + direction[0], self.position[1] + direction[1]]
            captured_position = self.get_captured_position(new_position)
            if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8:
                captured_piece = board[captured_position]
                if captured_piece != "_" and captured_piece.color != self.color:
                    return True
        return False
