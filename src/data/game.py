from board import Board
from player import Player


class Game:

    def __init__(self, board: Board, current_turn: Player):
        self.board = board
        self.current_turn = current_turn
        self.winner = None
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.current_turn.move(self.board)
            self.check_winner()
            self.current_turn = self.switch_turn()

    def check_winner(self):
        if self.current_turn.pieces == 0:
            self.winner = self.switch_turn()
            self.game_over = True

    def switch_turn(self) -> Player:
        if self.current_turn.color == "B":
            return Player("W")

        return Player("B")
