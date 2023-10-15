from BoardPieceHandler.BoardPieceHandler import BoardPieceHandler
from PieceFactory.BasicPieceFactory.BasicPieceFactory import BasicPieceFactory
from PieceGenerator.PieceGenerator import PieceGenerator
from board.Board import Board
from player.Player import Player
from team.Team import Team


class OptionalMethods(object):

    @staticmethod
    def is_piece_in_board(piece, board):
        return 0 <= piece.get_x() < board.get_width() and 0 <= piece.get_y() < board.get_height()


def test_piece_generator():
    isPieceInBoard = OptionalMethods.is_piece_in_board

    piece_factory = BasicPieceFactory()

    players1 = [Player("11", 1), Player("12", None, 2), Player("13"), Player("14")]
    players2 = [Player("21"), Player("22")]
    players3 = [Player("31"), Player("32"), Player("33")]

    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = [team1, team2, team3]

    bomb_count = 1
    coin_count = 2
    piece_handler = BoardPieceHandler()
    board = Board(4, 5, piece_handler)
    piece_generator = PieceGenerator(piece_factory)
    teams, bomb_pieces, coin_pieces = piece_generator.get_pieces_with_locations(teams,
                                                                                bomb_count,
                                                                                coin_count,
                                                                                board)

    # hec kesin locationi None olmasin ona bax
    # board'un icine sigir butun elementler ona bax. yeni board'un width height deyerlerine gore

    for team in teams:
        for player in team.get_players():
            piece = player.get_piece()

            if not piece.has_locations():
                raise Exception(player.get_name() + " x:" + str(piece.get_x()) +
                                " y:" + str(piece.get_y()))
            elif not isPieceInBoard(piece, board):
                raise Exception(player.get_name() + " x:" + str(piece.get_x()) +
                                " y:" + str(piece.get_y()) +
                                "board width:" + str(board.get_width()) +
                                "board height:" + str(board.get_height())
                                )

    for piece in bomb_pieces:
        if not piece.has_locations():
            raise Exception("Bomb piece " + " x:" + str(piece.get_x()) + " y:" + str(piece.get_y()))
        elif not isPieceInBoard(piece, board):
            raise Exception("Bomb piece " + " x:" + str(piece.get_x()) +
                            " y:" + str(piece.get_y()) +
                            "board width:" + str(board.get_width()) +
                            "board height:" + str(board.get_height())
                            )

    for piece in coin_pieces:
        if not piece.has_locations():
            raise Exception("Coin piece " + " x:" + piece.get_x() + " y:" + piece.get_y())
        elif not isPieceInBoard(piece, board):
            raise Exception("Coin piece " + " x:" + str(piece.get_x()) +
                            " y:" + str(piece.get_y()) +
                            "board width:" + str(board.get_width()) +
                            "board height:" + str(board.get_height())
                            )

    all_pieces = []
    for team in teams:
        for player in team.get_players():
            all_pieces.append(player.get_piece())

    all_pieces = all_pieces + bomb_pieces + coin_pieces

    for cur_piece in all_pieces:
        total = sum(
            1 for piece in all_pieces if cur_piece.get_x() == piece.get_x() and cur_piece.get_y() == piece.get_y())

        if total != 1:
            raise Exception(str(type(cur_piece)) + "X: " + str(cur_piece.get_x()) + "Y: " + str(cur_piece.get_y()))

