from Exceptions.PieceExistOnLocationOnBoardException import PieceExistOnLocationOnBoardException
from boardPiece import BoardPiece


class BoardPieceHandler(object):

    def __init__(self):
        self._board_pieces: list = []

    def add_piece(self, piece: BoardPiece, x: int, y: int):
        if x is not None and y is not None and \
                [x for piece in self._board_pieces if (piece.get_x() == x and piece.get_y() == y)]:
            raise PieceExistOnLocationOnBoardException('Piece exist on x: ' + str(x) + ' y: ' + str(y))

        piece.set_x(x)
        piece.set_y(y)
        self._board_pieces.append(piece)
        return piece

    def get_piece_at_location(self, x, y):
        lst = [piece for piece in self._board_pieces if x == piece.get_x() and y == piece.get_y()]

        if lst is not None and len(lst) > 0:
            return lst[0]
        return None
