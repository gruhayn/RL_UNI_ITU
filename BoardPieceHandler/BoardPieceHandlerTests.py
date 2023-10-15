from BoardPieceHandler.BoardPieceHandler import BoardPieceHandler
from Exceptions import PieceExistOnLocationOnBoardException
from boardPiece.BoardPiece import BoardPiece


def test_add_piece_returns_piece():
    handler = BoardPieceHandler()

    piece = handler.add_piece(BoardPiece(), 1, 2)
    assert piece.get_x() == 1
    assert piece.get_y() == 2


def test_add_piece_raises_exception():
    handler = BoardPieceHandler()

    piece = handler.add_piece(BoardPiece(), 1, 2)

    try:
        handler.add_piece(BoardPiece(), 1, 2)
    except PieceExistOnLocationOnBoardException.PieceExistOnLocationOnBoardException:
        pass
    except Exception:
        raise Exception("PieceExistOnLocationOnBoardException exceptioin is needed")
