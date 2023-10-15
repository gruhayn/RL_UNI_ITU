from PieceGenerator import PieceGenerator
from PlayerSelector import IPlayerSelector
from board import Board
from game.Game import Game


class GameCreator(object):

    def __init__(self,
                 teams: tuple,
                 board: Board,
                 bomb_count: int,
                 coin_count: int,
                 player_selector: IPlayerSelector,
                 piece_generator: PieceGenerator
                 ):
        self._teams = teams
        self._board = board
        self._bomb_count = bomb_count
        self._coin_count = coin_count
        self._player_selector = player_selector
        self._player_selector.set_teams(teams)
        self._piece_generator = piece_generator

    def create_new_game(self):

        self._teams, bomb_pieces, coin_pieces = self._piece_generator.get_pieces_with_locations(self._teams,
                                                                                                self._bomb_count,
                                                                                                self._coin_count,
                                                                                                self._board)

        for team in self._teams:
            for player in team.get_players():
                self._board.add_piece(player.get_piece())

        for piece in bomb_pieces + coin_pieces:
            self._board.add_piece(piece)

        game = Game(self._board, self._player_selector, self._teams)

        return game
