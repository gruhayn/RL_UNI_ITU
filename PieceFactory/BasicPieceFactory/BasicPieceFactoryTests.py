from PieceFactory.BasicPieceFactory.BasicPieceFactory import BasicPieceFactory
from boardPiece.BombBoardPiece import BombBoardPiece
from boardPiece.CoinBoardPiece import CoinBoardPiece


def test_create_coin_piece():
    basic_piece_factory = BasicPieceFactory()
    x = 1
    y = 2
    piece = basic_piece_factory.create_coin_piece(x, y)

    assert isinstance(piece, CoinBoardPiece.CoinBoardPiece) is True
    assert piece.get_x() == x
    assert piece.get_y() == y


def test_create_coin_piece():
    basic_piece_factory = BasicPieceFactory()
    x = 1
    y = 2
    piece = basic_piece_factory.create_bomb_piece(x, y)

    assert isinstance(piece, BombBoardPiece.BombBoardPiece) is True
    assert piece.get_x() == x
    assert piece.get_y() == y
