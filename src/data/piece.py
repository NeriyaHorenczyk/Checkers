class Piece:

    def __init__(self, color):
        self.color = color
        self.position = None
        self.king = False

    def move_king(self, board, new_position: tuple):
        # Implement the logic for moving a king piece
        if self.is_valid_king_move(board, new_position):
            self.position = new_position
            return True
        return False

    def move_regular(self, board, new_position: tuple):
        # Implement the logic for moving a regular piece
        if self.is_valid_regular_move(board, new_position):
            self.position = new_position
            if not self.king:
                self.promote()
            return True
        return False

    def capture(self, board, new_position: tuple):
        if self.is_valid_capture(board, new_position):
            self.position = new_position
            return True
        return False

    def promote(self):
        if self.position[0] == 0 and self.color == "B":
            self.king = True
        if self.position[0] == 7 and self.color == "W":
            self.king = True

    def is_valid_king_move(self, board, new_position: tuple) -> bool:
        # out of bounds
        if new_position[0] < 0 or new_position[0] > 7 or new_position[1] < 0 or new_position[1] > 7:
            return False

        # occupied
        if board[new_position[0]][new_position[1]] != "_":
            return False

        # not diagonal
        if abs(new_position[0] - self.position[0]) != abs(new_position[1] - self.position[1]):
            return False

        return True

    def is_valid_regular_move(self, board, new_position: tuple) -> bool:
        # out of bounds
        if new_position[0] < 0 or new_position[0] > 7 or new_position[1] < 0 or new_position[1] > 7:
            return False

        # occupied
        if board[new_position[0]][new_position[1]] != "_":
            return False

        # not diagonal
        if abs(new_position[0] - self.position[0]) != 1 or abs(new_position[1] - self.position[1]) != 1:
            return False

        return True

    def is_valid_capture(self, board, new_position: tuple) -> bool:
        # out of bounds
        if new_position[0] < 0 or new_position[0] > 7 or new_position[1] < 0 or new_position[1] > 7:
            return False

        # occupied
        if board[new_position[0]][new_position[1]] != "_":
            return False

        mid_x = (self.position[0] + new_position[0]) // 2
        mid_y = (self.position[1] + new_position[1]) // 2
        if board[mid_x][mid_y] == "_" or board[mid_x][mid_y] == self.color:
            return False
        if abs(new_position[0] - self.position[0]) != 2 or abs(new_position[1] - self.position[1]) != 2:
            return False
        return True
