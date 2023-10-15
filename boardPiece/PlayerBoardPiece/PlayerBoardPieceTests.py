from boardPiece.PlayerBoardPiece.PlayerBoardPiece import PlayerBoardPiece


def test_create_player_board_piece():
    piece = PlayerBoardPiece(None)
    assert piece is not None
    assert isinstance(piece, PlayerBoardPiece)


def test_check_player_board_piece_locations():
    piece = PlayerBoardPiece("name1")

    piece.set_x(1)
    piece.set_y(2)

    assert piece.get_x() == 1
    assert piece.get_y() == 2
    assert piece.get_name() == "name1"
