from boardPiece.CoinBoardPiece.CoinBoardPiece import CoinBoardPiece


def test_create_coin_board_piece():
    piece = CoinBoardPiece()

    assert piece is not None
    assert isinstance(piece, CoinBoardPiece)


def test_check_coin_board_piece_locations():
    piece = CoinBoardPiece()

    piece.set_x(1)
    piece.set_y(2)

    assert piece.get_x() == 1
    assert piece.get_y() == 2
