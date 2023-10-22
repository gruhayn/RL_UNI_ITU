# Game Creator Tests are in game > gameTest.py
from BoardPieceHandler.BoardPieceHandler import BoardPieceHandler
from Enums.Enums import Mechanics
from GameCreator.GameCreator import GameCreator
from MechanicFactory.MechanicFactory import MechanicFactory
from PieceFactory.BasicPieceFactory.BasicPieceFactory import BasicPieceFactory
from PieceGenerator.PieceGenerator import PieceGenerator
from PlayerSelector.TeamBasedSequentiallyPlayerSelector.TeamBasedSequentiallyPlayerSelector import \
    TeamBasedSequentiallyPlayerSelector
from board.Board import Board
from player.Player import Player
from team.Team import Team


def test_create_game_with_multi_team_multi_player_multi_mechanics_returns_multiple_mechanics_of_one_player():
    mf = MechanicFactory()
    mechanic_types = {
        Mechanics.MoveHorizontalOneStepMechanic,
        Mechanics.MoveHorizontalOneStepBackMechanic,
        Mechanics.MoveVerticalOneStepMechanic,
        Mechanics.MoveVerticalOneStepBackMechanic
    }

    players1 = [
        Player("11", 1, 1, mf, mechanic_types),
        Player("12", 1, 2, mf, mechanic_types),
        Player("13", 1, 3, mf, mechanic_types),
        Player("14", 1, 4, mf, mechanic_types)
    ]
    players2 = [
        Player("21", 2, 1, mf, mechanic_types),
        Player("22", 2, 2, mf, mechanic_types)
    ]
    players3 = [
        Player("31", 3, 1, mf, mechanic_types),
        Player("32", 3, 2, mf, mechanic_types),
        Player("33", 3, 3, mf, mechanic_types)
    ]

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

    player11: Player = game.select_next_player()

    #game.print_board()

    player11.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    #game.print_board()

    player11.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)
    #game.print_board()

    player11.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)
    #game.print_board()

    player11.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)
    #game.print_board()


def test_create_game_with_multi_team_multi_player_multi_mechanics_returns_multiple_mechanics_of_multi_player():
    mf = MechanicFactory()
    mechanic_types = {
        Mechanics.MoveHorizontalOneStepMechanic,
        Mechanics.MoveHorizontalOneStepBackMechanic,
        Mechanics.MoveVerticalOneStepMechanic,
        Mechanics.MoveVerticalOneStepBackMechanic
    }

    players1 = [
        Player("11", 1, 1, mf, mechanic_types),
        Player("12", 1, 2, mf, mechanic_types),
        Player("13", 1, 3, mf, mechanic_types),
        Player("14", 1, 4, mf, mechanic_types)
    ]
    players2 = [
        Player("21", 2, 1, mf, mechanic_types),
        Player("22", 2, 2, mf, mechanic_types)
    ]
    players3 = [
        Player("31", 3, 1, mf, mechanic_types),
        Player("32", 3, 2, mf, mechanic_types),
        Player("33", 3, 3, mf, mechanic_types)
    ]

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
    game.print_board()

    player11: Player = game.select_next_player()
    player11.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    game.print_board()

    player11: Player = game.select_next_player()
    player11.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    game.print_board()

