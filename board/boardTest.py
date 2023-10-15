from BoardPieceHandler.BoardPieceHandler import BoardPieceHandler
from board.Board import Board
from boardPiece.BoardPiece import BoardPiece


def test_create_board():
    width: int = 4
    height: int = 5
    board = Board(width, height, None)

    assert (width == board.get_width())
    assert (height == board.get_height())
    assert (width != board.get_height())
    assert (height != board.get_width())


def test_add_piece_to_board_board_piece_handler_doesnt_exist_returns_none():
    width: int = 4
    height: int = 5
    board = Board(width, height, None)

    assert (board.add_piece_with_locations(BoardPiece(), None, None) is False)


def test_add_piece_to_board_board_piece_handler_exist_returns_piece():
    width: int = 4
    height: int = 5

    board_piece_handler = BoardPieceHandler()
    board = Board(width, height, board_piece_handler)
    piece = BoardPiece()
    ret_piece = board.add_piece_with_locations(piece, None, None)

    assert (ret_piece is piece)


def test_add_piece_to_board_check_piece_locations():
    width: int = 4
    height: int = 5

    board_piece_handler = BoardPieceHandler()
    board = Board(width, height, board_piece_handler)
    piece = BoardPiece()
    ret_piece: BoardPiece = board.add_piece(piece, 1, 2)

    assert (ret_piece is piece)
    assert ret_piece.get_x() == 1
    assert ret_piece.get_y() == 2

def test_add_piece_to_board_check_piece_locations():
    width: int = 4
    height: int = 5

    board_piece_handler = BoardPieceHandler()
    board = Board(width, height, board_piece_handler)
    piece = BoardPiece()
    piece.set_x(1)
    piece.set_y(2)
    ret_piece: BoardPiece = board.add_piece(piece)

    assert (ret_piece is piece)
    assert ret_piece.get_x() == 1
    assert ret_piece.get_y() == 2
