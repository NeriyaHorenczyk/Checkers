class Piece:

    def __init__(self, color):
        self.color = color
        self.position = None

    def move(self, board, new_position):
        pass

    def capture(self, board, new_position):
        pass

    def is_valid_move(self, board, new_position):
        pass

    def is_valid_capture(self, board, new_position):
        pass
