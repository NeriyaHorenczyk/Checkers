from enum import Enum

from src.data.exeptions import InputError


class Color(Enum):
    WHITE = 'W'
    BLACK = 'B'
    EMPTY = '_'

class Piece:
    def __init__(self, color: Color, position: list[int]):
        self.color = color
        self.position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if not isinstance(new_position, list) or len(new_position) != 2:
            raise InputError("Position must be a list of two integers")
        print(f"Setting position to: {new_position}")
        self._position = new_position

    def move(self, board, new_position: list[int]) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses")

    def capture(self, board, new_position: tuple[int, int]) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses")

    def can_move(self, board) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses")

    def can_capture(self, board) -> bool:
        raise NotImplementedError("This method should be implemented by subclasses")

    def get_captured_position(self, new_position: list[int]) -> list[int]:
        return [(self.position[0] + new_position[0]) // 2, (self.position[1] + new_position[1]) // 2]
