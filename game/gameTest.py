from BoardPieceHandler.BoardPieceHandler import BoardPieceHandler
from Exceptions import PieceExistOnLocationOnBoardException
from GameCreator.GameCreator import GameCreator
from PieceFactory.BasicPieceFactory.BasicPieceFactory import BasicPieceFactory
from PieceGenerator.PieceGenerator import PieceGenerator
from PlayerSelector.TeamBasedSequentiallyPlayerSelector.TeamBasedSequentiallyPlayerSelector import \
    TeamBasedSequentiallyPlayerSelector
from board.Board import Board
from game.Game import Game
from player.Player import Player
from team.Team import Team


def test_create_game_and_game_is_started_false():
    game = Game(None, None, None)

    assert (False is game.is_started())


def test_start_game_game_is_started_true():
    game = Game(None, None, None)

    game.start()

    assert (True is game.is_started())


def test_select_next_player():
    players1 = [Player("11"), Player("12"), Player("13"), Player("14")]
    players2 = [Player("21"), Player("22")]
    players3 = [Player("31"), Player("32"), Player("33")]

    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = [team1, team2, team3]

    player_selector = TeamBasedSequentiallyPlayerSelector()
    piece_factory = BasicPieceFactory()
    piece_generator = PieceGenerator(piece_factory)
    piece_handler = BoardPieceHandler()

    game_creator = GameCreator(teams,
                               Board(4, 5, piece_handler),
                               1,  # bomb_count,
                               2,  # coin_count: int,
                               player_selector,
                               piece_generator)

    game = game_creator.create_new_game()

    selected_player_order = [
        "11",
        "21",
        "31",
        "12",
        "22",
        "32",
        "13",
        "21",
        "33",
        "14",
        "22",
        "31",
        "11",
        "21",
        "32"
    ]

    for i in selected_player_order:
        selected_player = game.select_next_player()
        assert (selected_player.get_name() == i)

    game.print_board()

def test_add_players_on_same_location_added():
    same_x = 1
    same_y = 2
    players1 = [
        Player("11", same_x, same_y),
        Player("12", 1, 3),
        Player("13", same_x, same_y),
        Player("14", 2, 3)
    ]

    players2 = [
        Player("21"),
        Player("22")
    ]
    players3 = [Player("31"), Player("32"), Player("33")]

    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = (team1, team2, team3)

    player_selector = TeamBasedSequentiallyPlayerSelector()

    width: int = 4
    height: int = 5

    board_piece_handler = BoardPieceHandler()
    board = Board(width, height, board_piece_handler)

    try:
        game = Game(board, player_selector, teams)
    except PieceExistOnLocationOnBoardException.PieceExistOnLocationOnBoardException as ex:
        pass
    except Exception:
        raise "PieceExistOnLocationOnBoard exception is expected"


def test_add_players_on_different_location_added():
    players1 = [
        Player("11", 1, 2),
        Player("12", 2, 1),
        Player("13", 2, 2),
        Player("14", 1, 1)
    ]

    players2 = [
        Player("21"),
        Player("22")
    ]
    players3 = [Player("31"), Player("32"), Player("33")]

    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = (team1, team2, team3)

    player_selector = TeamBasedSequentiallyPlayerSelector()

    width: int = 4
    height: int = 5

    board_piece_handler = BoardPieceHandler()
    board = Board(width, height, board_piece_handler)

    try:
        game = Game(board, player_selector, teams)
    except PieceExistOnLocationOnBoardException.PieceExistOnLocationOnBoardException as ex:
        raise Exception("game test PieceExistOnLocationOnBoard exception is not expected")
    except Exception:
        raise Exception("game Test another exception occured")

