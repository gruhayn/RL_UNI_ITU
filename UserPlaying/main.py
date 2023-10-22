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


def print_mechanics():
    for index_i in range(len(list(mechanic_types))):
        print(index_i, list(mechanic_types)[index_i], mf.get_formal_mechanic(list(mechanic_types)[index_i]).get_description())


while 1:
    player: Player = game.select_next_player()
    print("Player name: " + player.get_name())
    print_mechanics()
    index = int(input("Index mechanic:"))
    player.execute_mechanic(list(mechanic_types)[index])
    game.print_board()
