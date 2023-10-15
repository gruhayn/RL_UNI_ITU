from PieceGenerator import PieceGenerator
from PlayerSelector import IPlayerSelector
from board import Board
from player import Player


class Game(object):

    def __init__(self, board: Board, player_selector: IPlayerSelector, teams: tuple):
        self._is_started = False
        self._board: Board = board
        self._player_selector = player_selector

    def select_next_player(self):
        return self._player_selector.select_next_player()

    def is_started(self):
        return self._is_started

    def start(self):
        self._is_started = True

    def print_board(self):
        self._board.print_board()
