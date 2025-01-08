from src.data.board import Board
from src.data.piece import Piece, Color
from src.data.player import Player
from src.data.exeptions import TurnException

class Game:
    def __init__(self, board : Board = Board(), player : Player = Player.WHITE, default_white_pieces: int = 12,
                 default_black_pieces: int = 12):
        self.board = board
        self.white_pieces = default_white_pieces
        self.black_pieces = default_black_pieces

        self.current_turn = player

    def switch_turn(self):
        self.current_turn = Player.WHITE if self.current_turn == Player.BLACK else Player.BLACK

    def enforce_mandatory_capture(self):
        for row in range(8):
            for col in range(8):
                piece = self.board[[row, col]]
                if isinstance(piece, Piece) and piece.color == self.current_turn:
                    if piece.can_capture(self.board):
                        return True
        return False

    def is_game_over(self) -> bool:
        if self.white_pieces == 0 or self.black_pieces == 0 or not self.has_valid_moves(self.current_turn):
            return True
        return False

    def has_valid_moves(self, player: Player) -> bool:
        for row in range(8):
            for col in range(8):
                piece = self.board[[row, col]]
                if isinstance(piece, Piece) and piece.color == player.value:
                    if piece.can_move(self.board) or piece.can_capture(self.board):
                        return True
        return False

    def make_move(self, player: Player, piece: Piece, new_position: tuple[int, int]):
        if player != self.current_turn:
            raise TurnException("It's not your turn")

        if piece.capture(self.board, new_position):
            self._update_piece_count(piece)

        else:
            if not piece.move(self.board, new_position):
                raise TurnException("Invalid move")

        if not piece.can_capture(self.board):
            self.switch_turn()

    def _update_piece_count(self, piece: Piece):
        captured_position = piece.get_captured_position(piece.position)
        captured_piece = self.board[captured_position]
        if captured_piece.color == Player.WHITE.value:
            self.white_pieces -= 1
        elif captured_piece.color == Player.BLACK.value:
            self.black_pieces -= 1
        self.board[captured_position] = Piece(Color.EMPTY, captured_position)

    def get_winner(self) -> Player | None:
        if not self.white_pieces or not self.has_valid_moves(self.current_turn):
            return Player.BLACK
        if self.black_pieces == 0 or not self.has_valid_moves(self.current_turn):
            return Player.WHITE
        return None
