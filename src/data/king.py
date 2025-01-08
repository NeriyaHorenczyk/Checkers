from src.data.piece import Piece

class King(Piece):


    def move(self, board, new_position: list[int]) -> bool:
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])

        if row_diff == col_diff and board[new_position] == "_":
            self.position = new_position
            return True
        return False

    def capture(self, board, new_position: tuple[int, int]) -> bool:
        row_diff = abs(new_position[0] - self.position[0])
        col_diff = abs(new_position[1] - self.position[1])

        if row_diff == 2 and col_diff == 2:
            captured_position = ((self.position[0] + new_position[0]) // 2, (self.position[1] + new_position[1]) // 2)
            captured_piece = board[captured_position]

            if captured_piece != "_" and captured_piece.color != self.color:
                self.position = new_position
                board[captured_position] = "_"
                return True
        return False

    def can_move(self, board) -> bool:
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
            if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8 and board[new_position] == "_":
                return True
        return False


    def can_capture(self, board) -> bool:
        directions = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
        for direction in directions:
            new_position = [self.position[0] + direction[0], self.position[1] + direction[1]]
            captured_position = self.get_captured_position(new_position)
            if 0 <= new_position[0] < 8 and 0 <= new_position[1] < 8:
                captured_piece = board[captured_position]
                if captured_piece != "_" and captured_piece.color != self.color:
                    return True
        return False
