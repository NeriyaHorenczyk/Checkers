from src.data.piece import Piece


class Board:

    default_board = [
                ["B", "_", "B", "_", "B", "_", "B", "_"],
                ["_", "B", "_", "B", "_", "B", "_", "B"],
                ["B", "_", "B", "_", "B", "_", "B", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "_", "_", "_", "_", "_", "_", "_"],
                ["_", "W", "_", "W", "_", "W", "_", "W"],
                ["W", "_", "W", "_", "W", "_", "W", "_"],
                ["_", "W", "_", "W", "_", "W", "_", "W"]
                ]

    def __init__(self, board : list[list[Piece]] = None):
        if not board:
            self.board = self.default_board
        else:
            self.board = board

    def __getitem__(self, position : list[int]) -> Piece:
        return self.board[position[0]][position[1]]

    def __setitem__(self, position : list[int], value : Piece):
        self.board[position[0]][position[1]] = value
