from boardPiece.BombBoardPiece.BombBoardPiece import BombBoardPiece


def test_create_bomb_board_piece():
    piece = BombBoardPiece()

    assert piece is not None
    assert isinstance(piece, BombBoardPiece)


def test_check_bomb_board_piece_locations():
    piece = BombBoardPiece()

    piece.set_x(1)
    piece.set_y(2)

    assert piece.get_x() == 1
    assert piece.get_y() == 2
