from boardPiece import BoardPiece
from boardPiece.PlayerBoardPiece.PlayerBoardPiece import PlayerBoardPiece


class Player(object):
    def __init__(self, name: str, x: int = None, y: int = None):
        self._name = name
        self._board_piece = PlayerBoardPiece(name)
        self.set_piece_x(x)
        self.set_piece_y(y)

    def get_name(self) -> str:
        return self._name

    def get_piece(self):
        return self._board_piece

    def set_piece_x(self, x):
        self._board_piece.set_x(x)

    def set_piece_y(self, y):
        self._board_piece.set_y(y)


