from pathlib import Path
import yaml

from src.data.board import Board
from src.data.king import King
from src.data.pawn import Pawn
from src.data.piece import Color


# Function to get the YAML directory
def get_yaml_dir() -> Path:
    return Path(__file__).parent / 'yaml_test_case'


# Function to load a YAML file
def load_yaml(yaml_file: Path) -> dict:
    with open(yaml_file, 'r') as f:
        return yaml.safe_load(f)


def test_init_board():
    data = load_yaml(get_yaml_dir() / 'init_board.yaml')
    game_data = data.get("game", {})
    board_data = game_data.get("board", {})
    board = Board()
    assert board.board == board_data

def test_position_setter():
    pawn_piece = Pawn(Color.BLACK, [3, 0])
    king_piece = King(Color.BLACK, [0, 0])
    board = Board()
    pawn_piece.move(board, [4, 1])
    king_piece.move(board, [1, 1])


def test_eat_piece():
    pass
