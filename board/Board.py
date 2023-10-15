from BoardPieceHandler import BoardPieceHandler
from boardPiece import BoardPiece
from boardPiece.BombBoardPiece import BombBoardPiece
from boardPiece.CoinBoardPiece import CoinBoardPiece
from boardPiece.PlayerBoardPiece import PlayerBoardPiece


class Board(object):

    def __init__(self, width: int, height: int, piece_handler: BoardPieceHandler):
        self._width: int = width
        self._height: int = height
        self._piece_handler: BoardPieceHandler = piece_handler

    def add_piece_with_locations(self, piece: BoardPiece, x: int, y: int) -> BoardPiece:
        return False if self._piece_handler is None else self._piece_handler.add_piece(piece, x, y)

    def add_piece(self, piece: BoardPiece) -> BoardPiece:
        return self.add_piece_with_locations(piece, piece.get_x(), piece.get_y())

    def get_width(self) -> int:
        return self._width

    def get_height(self) -> int:
        return self._height

    def print_board(self):
        for x in range(0, self._width):
            for y in range(self._height - 1, -1, -1):
                piece = self._piece_handler.get_piece_at_location(x, y)
                if piece is not None:
                    print("x: " + str(x) + " y: " + str(y) + " " + str(type(piece)))

        for y in range(self._height - 1, -1, -1):
            for x in range(0, self._width):
                piece = self._piece_handler.get_piece_at_location(x, y)
                if piece is None:
                    print("*   " , end="")

                if isinstance(piece, PlayerBoardPiece.PlayerBoardPiece):
                    print('{: <4}'.format(piece.get_name()), end="")
                elif isinstance(piece, BombBoardPiece.BombBoardPiece):
                    print("B   ", end="")
                elif isinstance(piece, CoinBoardPiece.CoinBoardPiece):
                    print("C   ", end="")
            print()
