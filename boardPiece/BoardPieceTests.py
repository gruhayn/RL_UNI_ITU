from boardPiece.BoardPiece import BoardPiece


def test_set_board_piece_locations():
    piece = BoardPiece()

    assert (piece.get_x() is None)
    assert (piece.get_y() is None)
    assert piece.has_locations() is False

    piece.set_x(10)

    assert (piece.get_x() == 10)
    assert (piece.get_y() is None)
    assert piece.has_locations() is False

    piece.set_y(15)

    assert (piece.get_x() == 10)
    assert (piece.get_y() == 15)
    assert piece.has_locations() is True

    piece.set_x(12)

    assert (piece.get_x() == 12)
    assert (piece.get_y() == 15)
    assert piece.has_locations() is True
