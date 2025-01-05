from src.data.board import Board
from src.data.player import Player


class Game():
    WHITE = 'W'
    BLACK = 'B'
    EMPTY = '_'

    def __init__(self, default_white_pieces: int = 12, default_black_pieces: int = 12):
        self.board = Board()
        self.white_pieces = default_white_pieces
        self.black_pieces = default_black_pieces

        self.players = [Player('W', default_white_pieces), Player('B', default_black_pieces)]
        self.current_turn: Player | None = self.players[0]

    def switch_turn(self):
        pass

    def is_game_over(self):
        return any(player.pieces == 0 for player in self.players)

    def make_move(self, player, piece, new_position):
        if player.color != self.current_turn:
            raise ValueError("It's not your turn")

        if piece.move(self.board, new_position):
            self.switch_turn()
        elif piece.capture(self.board, new_position):
            self.switch_turn()
            player.pieces -= 1

        else:
            raise ValueError("Invalid move")

    def get_winner(self):
        if self.is_game_over():
            for player in self.players:
                if player.pieces > 0:
                    return player.color
        return None
